from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load movie data and similarity matrix
movies = pickle.load(open('models\movies.pkl', 'rb'))
similarity = pickle.load(open('models\similarity.pkl', 'rb'))

# Convert to DataFrame if necessary
if isinstance(movies, dict):
    movies = pd.DataFrame(movies)

# Recommend function
def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

@app.route('/')
def home():
    return render_template('index.html', movie_list=movies['title'].values)

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    movie_name = request.form['movie']
    recommended_movie_names = recommend(movie_name)
    return render_template('index.html', movie_list=movies['title'].values, recommendations=recommended_movie_names, selected_movie=movie_name)

if __name__ == '__main__':
    app.run(debug=True)
