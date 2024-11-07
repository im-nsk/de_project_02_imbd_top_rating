import pandas as pd  # Load the CSV file

file_path = 'path_to_your_file.csv'
df = pd.read_csv(file_path)

print(df.head())  # View the first few rows of the dataset
print(df.info())  # Get an overview of the dataset's columns and data types
print(df.describe())  # Get summary statistics for numeric columns


# Clean 'genres' by removing leading/trailing spaces and commas
df['genres'] = df['genres'].str.strip().str.rstrip(',')

# Split genres into multiple rows and strip extra whitespace
df_genres = df.assign(genres=df['genres'].str.split(',')).explode('genres')
df_genres['genres'] = df_genres['genres'].str.strip()  # Remove extra whitespace

# Standardize column names (e.g., lowercase and replace spaces with underscores)
df_genres.columns = df_genres.columns.str.lower().str.replace(' ', '_')

# Convert releaseYear to datetime
df_genres['releaseYear'] = pd.to_datetime(df_genres['releaseYear'], format='%Y')

# Add decade column based on releaseYear
df_genres['decade'] = (df_genres['releaseYear'].dt.year // 10) * 10
