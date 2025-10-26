import streamlit as st
import pandas as pd
import requests
import pickle
import time

# Load movie data and similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Recommendation function
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

# Fetch poster from TMDB safely
def fetch_poster(movie_id):
    api_key = '6378939bb894b897cb5cfba39fe59b36'
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # handle HTTP errors (404, 500, etc.)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f'https://image.tmdb.org/t/p/w500{poster_path}'
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error+Loading"

# Streamlit UI
st.title('🎬 Movie Recommendation System')

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)
    st.write("### Top 10 Recommended Movies:")

    # Display posters in a grid (2 rows x 5 columns)
    for i in range(0, 10, 5):
        cols = st.columns(5)
        for col, j in zip(cols, range(i, i + 5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]['title']
                movie_id = recommendations.iloc[j]['movie_id']
                poster_url = fetch_poster(movie_id)
                with col:
                    st.image(poster_url, width=130)
                    st.caption(movie_title)
                time.sleep(0.3)  # small delay to avoid too many rapid API calls
