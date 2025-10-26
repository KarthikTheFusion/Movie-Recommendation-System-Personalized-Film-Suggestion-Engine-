# 🎬 Movie Recommendation System – Personalized Film Suggestion Engine

An AI-powered, interactive movie recommendation web app built using **Streamlit**, **Machine Learning**, and **The Movie Database (TMDB) API**.  
This project delivers **personalized film suggestions** by analyzing content similarities between movies — helping users discover their next favorite film effortlessly!

---

## 🚀 Features

- 🎯 **Personalized Recommendations:** Suggests top 10 similar movies based on your selected title.  
- 🧠 **Machine Learning-Powered:** Uses cosine similarity on feature vectors for accurate content-based recommendations.  
- 🖼️ **Dynamic Posters:** Fetches real-time movie posters via TMDB API.  
- ⚡ **Lightweight & Fast:** Optimized with caching and efficient API calls.  
- 🖥️ **Streamlit UI:** Clean, responsive, and beginner-friendly web interface.

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| Frontend | Streamlit |
| Backend | Python |
| Machine Learning | Cosine Similarity (Content-Based Filtering) |
| Data Handling | Pandas, Pickle |
| API | The Movie Database (TMDB) |
| Deployment | Streamlit Cloud / Localhost |

---

## 📦 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/MovieRecommendationSystem.git
   cd MovieRecommendationSystem
Install required dependencies
bash
pip install -r requirements.txt
Add your TMDB API key

Open app.py
Replace:
python
api_key = 'YOUR_API_KEY'
with your own key from TMDB API.

Run the app
'''bash
streamlit run app.py
Enjoy personalized movie recommendations! 🍿

🧠 How It Works
The dataset of movies is preprocessed and feature vectors are generated using text-based metadata (like genre, director, keywords, etc.).
Cosine similarity measures how similar two movies are.
When a user selects a movie, the system recommends the top 10 most similar movies.
Posters are fetched dynamically from TMDB API for a rich visual experience.

🖼️ Example Output
Input Movie: Inception
Recommended Movies: Interstellar, The Prestige, Memento, Shutter Island, etc.
Each recommendation includes movie title and poster image.

```bash
MovieRecommendationSystem/
│
├── app.py                 # Main Streamlit app file
├── movie_data.pkl         # Preprocessed movie data + cosine similarity matrix
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── assets/                # (Optional) Icons, screenshots, or visuals


🧩 Requirements
Python 3.8+
Streamlit
Pandas
Requests
Pickle

You can install them all via:
'''bash
pip install streamlit pandas requests

🌐 API Reference
TMDB API: https://developers.themoviedb.org/3

💡 Future Enhancements
🎞️ Add user-based collaborative filtering
🔍 Include search and genre-based filtering
🧩 Cache poster URLs for faster loading
📱 Make it mobile-responsive

🤝 Contributing
Contributions are welcome!
If you'd like to improve this project, feel free to:
Fork this repository
Create a new branch
Submit a pull request 🚀
