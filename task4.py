import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Sample data: User ratings for movies
data = {
    'User': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Charlie', 'Charlie', 'Charlie', 'David', 'David'],
    'Movie': ['Inception', 'Titanic', 'Avatar', 'Inception', 'Avatar', 'Inception', 'Titanic', 'Avatar', 'Titanic', 'Avatar'],
    'Rating': [5, 4, 4, 5, 4, 4, 5, 5, 3, 4]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Pivot the DataFrame to create a user-item matrix
user_movie_matrix = df.pivot_table(index='User', columns='Movie', values='Rating')

# Fill NaN with 0 (Assume missing ratings are 0 for simplicity)
user_movie_matrix = user_movie_matrix.fillna(0)

print("User-Movie Matrix:")
print(user_movie_matrix)

# Standardize the data (necessary for cosine similarity)
scaler = StandardScaler()
scaled_matrix = scaler.fit_transform(user_movie_matrix)

# Compute cosine similarity between users
user_similarity = cosine_similarity(scaled_matrix)

# Convert similarity matrix to a DataFrame for readability
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

print("\nUser Similarity Matrix:")
print(user_similarity_df)

# Function to recommend movies for a given user
def recommend_movies(user, num_recommendations=3):
    similar_users = user_similarity_df[user].sort_values(ascending=False)
    user_ratings = user_movie_matrix.loc[user]

    # Find movies the user hasn't rated yet
    unrated_movies = user_ratings[user_ratings == 0].index
    
    recommendations = pd.Series(dtype=float)
    
    # Predict ratings for unrated movies based on ratings from similar users
    for movie in unrated_movies:
        weighted_sum = 0
        similarity_sum = 0
        
        for similar_user in similar_users.index:
            if user_movie_matrix.loc[similar_user, movie] > 0:  # Only consider users who rated this movie
                weighted_sum += user_similarity_df.loc[user, similar_user] * user_movie_matrix.loc[similar_user, movie]
                similarity_sum += user_similarity_df.loc[user, similar_user]
        
        if similarity_sum > 0:
            predicted_rating = weighted_sum / similarity_sum
            recommendations[movie] = predicted_rating
    
    # Sort the recommendations by predicted rating and return the top N
    return recommendations.sort_values(ascending=False).head(num_recommendations)

# Test the recommendation function
user = 'Alice'
print(f"\nRecommended movies for {user}:")
print(recommend_movies(user, num_recommendations=3))
