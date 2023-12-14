import numpy as np
from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Sample user preferences data
user_preferences = {
    'User1': {'Action': 5, 'Comedy': 4, 'Drama': 2},
    'User2': {'Action': 3, 'Comedy': 5, 'Drama': 4},
    'User3': {'Action': 1, 'Comedy': 2, 'Drama': 5},
}

# Sample content data
content_data = {
    'Movie1': {'Action': 4, 'Comedy': 2, 'Drama': 3},
    'Movie2': {'Action': 5, 'Comedy': 3, 'Drama': 4},
    'Movie3': {'Action': 2, 'Comedy': 4, 'Drama': 5},
}

# Convert data to pandas DataFrames
users_df = pd.DataFrame.from_dict(user_preferences, orient='index')
content_df = pd.DataFrame.from_dict(content_data, orient='index')

# Calculate cosine similarity between users and content
user_content_similarity = cosine_similarity(users_df, content_df)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    user_name = request.form.get('user')

    if user_name not in user_preferences:
        return render_template('index.html', error='User not found')

    user_index = list(user_preferences.keys()).index(user_name)
    user_similarity_scores = user_content_similarity[user_index]

    # Get content recommendations based on similarity scores
    content_recommendations = content_df.index[np.argsort(user_similarity_scores)[::-1]]

    return render_template('recommendations.html', user=user_name, recommendations=content_recommendations)

if __name__ == '__main__':
    app.run(debug=True)
