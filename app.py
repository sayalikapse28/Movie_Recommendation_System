import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

movies = pickle.load(open('movies.pkl','rb'))

st.set_page_config(page_title="Movie Recommender", layout="centered")
st.title("🎬 AI Movie Recommendation System")

# Recreate vectors and similarity
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

selected_movie = st.selectbox("Select a movie", movies['title'].values)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

if st.button("Recommend"):
    for movie in recommend(selected_movie):
        st.write("👉", movie)
