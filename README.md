# 🎬 AI Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on textual features such as genres, overview, keywords, cast, and crew.  
Built using Python and deployed as an interactive web app using Streamlit.

---

## 🚀 Live Demo

App Link:  
https://movierecommendationsystem-drgoyfmxgsewzmkwby9s39.streamlit.app/?embed_options=dark_theme

GitHub Repository:  
https://github.com/sayalikapse28/Movie_Recommendation_System/

---

## 🧠 How It Works

1. Movie metadata is loaded from the TMDB 5000 Movies Dataset.  
2. Important features are extracted:
   - Overview  
   - Genres  
   - Keywords  
   - Top 3 Cast members  
   - Director  
3. All features are combined into a single text column called `tags`.  
4. Text is converted into numerical vectors using TF-IDF Vectorization.  
5. Cosine Similarity is applied to compute similarity between movies.  
6. Based on the selected movie, top similar movies are recommended.

---

## 📊 Dataset

TMDB 5000 Movies Dataset from Kaggle  
Files used:
- tmdb_5000_movies.csv  
- tmdb_5000_credits.csv  

Dataset Link:  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 🛠 Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn (TF-IDF, Cosine Similarity)  
- Streamlit  
- Pickle  

---

## 📁 Project Structure

Movie_Recommendation_System/  
├── app.py  
├── movies.pkl  
├── requirements.txt  
└── notebook/  
    └── movie_recommendation.ipynb  

---

## ▶️ How to Run Locally

### 1. Clone Repository

git clone https://github.com/sayalikapse28/Movie_Recommendation_System.git  
cd Movie_Recommendation_System  

### 2. Install Dependencies

pip install -r requirements.txt  

### 3. Run Streamlit App

streamlit run app.py  

App will open at: http://localhost:8501

---

## 📌 Features

- Content-based movie recommendation  
- TF-IDF based text vectorization  
- Cosine similarity for ranking movies  
- Simple and interactive UI  
- Cloud deployed application  

---

## 🔮 Future Improvements

- Show movie posters using TMDB API  
- Add collaborative filtering using ratings data  
- Improve similarity using embeddings  
- Build FastAPI backend for recommendations  
- Add user personalization  

---

## 🙋‍♀️ Author

Sayali Kapse  
Software Engineer | Aspiring AI Engineer  

GitHub: https://github.com/sayalikapse28

---

⭐ If you find this project useful, consider giving it a star!
