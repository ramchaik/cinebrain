import os
import requests
import pandas as pd
import numpy as np

processed_df = pd.read_pickle('data/processed_df.pkl')
similarity = np.load('data/similarity.npy')

def recommend(movie):
    movie_idx = processed_df[processed_df['title'] == movie].index[0]
    distances = similarity[movie_idx]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for m in movie_list:
        movie_details = fetch_movie_details(processed_df.iloc[m[0]].movie_id)
        recommended_movies.append(movie_details)
        
    return recommended_movies

def fetch_movie_details(movie_id):
    api_key = os.getenv('TMDB_API_KEY')
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def get_movie_titles():
    return processed_df['title'].tolist()

