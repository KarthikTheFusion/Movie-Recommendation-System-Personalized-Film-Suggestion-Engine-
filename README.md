# 🎬 Movie Recommendation System – Personalized Film Suggestion Engine

An **AI-powered web application** that delivers **personalized movie recommendations** based on content similarity.  
Built using **Python, Streamlit**, and **The Movie Database (TMDB) API**, it enhances the movie discovery experience with intelligent suggestions and dynamic visuals.

---

## 🚀 Overview

The **Movie Recommendation System** analyzes movie metadata and computes similarity using **cosine similarity** to suggest films related to a user’s chosen title.  
It provides an intuitive, interactive interface that displays both movie titles and posters in real time.

---

## ✨ Key Features

- 🎯 **Smart Recommendations:** Suggests top 10 similar movies using machine learning.  
- 🖼️ **Real-Time Posters:** Fetches movie posters via TMDB API.  
- 🧠 **Content-Based Filtering:** Uses textual and categorical data to compute similarity.  
- ⚡ **Lightweight & Fast:** Optimized requests with caching and fallback handling.  
- 💻 **Interactive UI:** Built with Streamlit for an engaging user experience.

---

## 🧩 Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Frontend/UI** | Streamlit |
| **Backend Logic** | Python |
| **Data Processing** | Pandas, Pickle |
| **Machine Learning** | Cosine Similarity (Content-Based Filtering) |
| **API Integration** | TMDB API |

---

## ⚙️ Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/MovieRecommendationSystem.git
cd MovieRecommendationSystem

2. Install Dependencies
pip install -r requirements.txt

3. Set Up API Key

Get your API key from TMDB
.

Open app.py and replace:

api_key = 'YOUR_API_KEY'

4. Run the App
streamlit run app.py

🧠 How It Works

Data Preparation:
The dataset is preprocessed, and movie metadata is vectorized.

Similarity Calculation:
Uses cosine similarity to measure closeness between movies based on content attributes.

Recommendation Generation:
When a user selects a movie, the system retrieves the top 10 most similar titles.

Poster Retrieval:
Fetches and displays posters dynamically via TMDB API for a visually rich interface.

📁 Project Structure
MovieRecommendationSystem/
│
├── app.py                 # Main Streamlit application
├── movie_data.pkl         # Preprocessed movie dataset and similarity matrix
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── assets/                # (Optional) Screenshots or visuals

📸 Example

Input: Inception
Output: Interstellar, The Prestige, Memento, Shutter Island, etc.
Each result displays the movie title and its poster image fetched from TMDB.

🔧 Requirements

Python 3.8+

Streamlit

Pandas

Requests

Pickle

Install all dependencies via:

pip install streamlit pandas requests

🌟 Future Improvements

🔍 Add user-based collaborative filtering

🎞️ Include genre and actor-based search filters

💾 Cache poster URLs for faster load times

📱 Improve mobile responsiveness

🤝 Contributing

Contributions, suggestions, and feature requests are always welcome!
To contribute:

Fork this repository

Create a new branch

Submit a pull request 🚀
