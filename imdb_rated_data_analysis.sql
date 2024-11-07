-- With the data now in PostgreSQL, you can run SQL queries to extract meaningful insights from it.

-- 1. Top 5 Most Popular Genres by the Number of Movies:
SELECT genres, COUNT(*) AS movie_count
FROM movies
GROUP BY genres
ORDER BY movie_count DESC
LIMIT 5;

-- 2. Average Rating per Genre:
-- This query will help you understand which genres tend to have the highest ratings.
SELECT genres, AVG(averageRating) AS avg_rating
FROM movies
GROUP BY genres
ORDER BY avg_rating DESC;

-- 3. Genre Popularity by Decade:
-- This query shows how the popularity of genres has changed over the decades.
SELECT decade, genres, COUNT(*) AS movie_count
FROM movies
GROUP BY decade, genres
ORDER BY decade, movie_count DESC;

-- 4. Most Popular Movies by Votes:
-- Here, we identify the movies with the highest number of votes across all genres.
SELECT title, genres, numVotes
FROM movies
ORDER BY numVotes DESC
LIMIT 10;