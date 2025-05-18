import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the Movie Data (ensure the column name matches your CSV file)
try:
    df = pd.read_csv("C:/Users/ADMIN/Documents/Python/CODSOFT/movies.csv")
    print("File loaded successfully with UTF-8 encoding.")
except UnicodeDecodeError:
    try:
        df = pd.read_csv("C:/Users/ADMIN/Documents/Python/CODSOFT/movies.csv")
        print("File loaded successfully with Latin-1 encoding.")
    except UnicodeDecodeError:
        try:
            df = pd.read_csv("C:/Users/ADMIN/Documents/Python/CODSOFT/movies.csv")
            print("File loaded successfully with CP1252 encoding.")
        except UnicodeDecodeError as e:
            print(f"Error loading file with various encodings: {e}")
            exit()

# Step 2: Inspect the Data (optional, for debugging)
print(df.columns)  # Check the columns to make sure we have the right ones
print(df.head())    # Check first few rows of the dataset

# Print unique titles to help identify the correct title
print("Unique movie titles in the dataset:")
print(df['title'].unique())

# Step 3: Preprocess Data (replace NaN descriptions with empty strings)
df['description'] = df['description'].fillna('')

# Step 4: Use TfidfVectorizer to transform the text (movie descriptions)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Step 5: Compute Cosine Similarity between movies based on their descriptions
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Step 6: Create a function to recommend movies based on a given movie title
def recommend(title, cosine_sim=cosine_sim):
    # Check if the title exists in the DataFrame
    if title not in df['title'].values:
        print(f"Error: Movie '{title}' not found in the dataset.")
        return None  # Or some other appropriate return value

    # Get the index of the movie that matches the title
    idx = df[df['title'] == title].index[0]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 similar movies (excluding the first one which is the same movie)
    sim_scores = sim_scores[1:6]

    # Get the movie indices and return the titles of the recommended movies
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Example: Get recommendations for a movie (e.g., "The Dark Knight")
movie_to_recommend = 'The Dark Knight'  # Make sure this title exactly matches one in your dataset
recommended_movies = recommend(movie_to_recommend)

if recommended_movies is not None:
    print(f"\nRecommended Movies for '{movie_to_recommend}':")
    print(recommended_movies)
