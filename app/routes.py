from flask import Blueprint, request, jsonify, render_template
from .recommender import recommend, fetch_movie_details, get_movie_titles

import pandas as pd

main = Blueprint('main', __name__)

processed_df = pd.read_pickle('data/processed_df.pkl')

@main.route('/')
def index():
    movie_titles = get_movie_titles()
    return render_template('index.html', movies=movie_titles)

@main.route('/movies', methods=['GET'])
def get_movies():
    movie_titles = get_movie_titles()
    return jsonify(movie_titles)

@main.route('/movie/<int:movie_id>', methods=['GET'])
def get_movie_details(movie_id):
    movie_details = fetch_movie_details(movie_id)
    if movie_details:
        return jsonify(movie_details)
    else:
        return jsonify({'error': 'Movie not found'}), 404

@main.route('/recommend', methods=['POST'])
def recommend_movies():
    movie_title = request.form['selected_movie']
    
    recommended_movies_details = recommend(movie_title)

    if not recommended_movies_details:
        return "", 204 
    
    selected_movie_details = fetch_movie_details(processed_df.loc[processed_df['title'] == movie_title, 'movie_id'].values[0])
    
    return render_template('recommendations_partial.html', 
                           selected_movie=selected_movie_details, 
                           recommended_movies=recommended_movies_details)
