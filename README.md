# de_project_02_imbd_top_rating

As promised, we're kicking off the Live Data Engineering Project Session! We’ll cover everything from scratch to advanced, building an end-to-end data pipeline.

Find me: https://www.linkedin.com/in/im-nsk/

Welcome to our second project session! In this project, we will analyze IMDb's top-rated movies dataset using Python and SQL. The goal is to load, clean, transform, and analyze the data to derive meaningful insights about movie genres, ratings, trends, and customer preferences over time.

The project will involve:

Python for data reading, manipulation, table creation, loading (using pandas).
SQL for storing and querying the data in a PostgreSQL database.
ETL (Extract, Transform, Load) operations to transform raw data into structured, analyzable information.

#### Steps to Complete the Project:

**Step 1: Set Up Your Environment**
Make sure you have the necessary Python libraries installed to manipulate the dataset and interact with PostgreSQL.

**Step 2: Read the CSV File Using Pandas**
Load the dataset into a pandas DataFrame to start working with it.

**Step 3: Data Exploration and Cleaning**
Explore the data to understand its structure and identify any data quality issues (e.g., missing values, inconsistencies).

**Basic Data Cleaning Steps:**
1. **Check for Missing Values** and handle them (e.g., fill or drop).
2. **Convert Data Types** as necessary (e.g., convert `releaseYear` to integer).
3. **Clean the 'genres' Column** by removing leading or trailing spaces and commas.

**Step 4: Data Transformation**
Transform the dataset to make it more structured and insightful.

**1. Split the `genres` Column**
Since movies can have multiple genres, we will split the `genres` column into individual rows for each genre.
**2. Additional Transformations**

- **Standardize Column Names:** Make column names lowercase and replace spaces with underscores.
- **Convert `releaseYear` to DateTime Format:** This makes it easier to handle dates for analysis.
- **Calculate Decade:** Calculate the decade for each movie based on the `releaseYear`.


---
**Step 5: Connect to PostgreSQL and Load Data**

Now, we'll connect to a PostgreSQL database and insert the cleaned and transformed data.
  
**1. Connect to PostgreSQL:**
Use `psycopg2` to connect to your database.

**2. Insert Data into PostgreSQL:**
Loop through the DataFrame and insert each record into the `movies` table.

---

### **Step 6: Extract Insights**

With the data now in PostgreSQL, you can run SQL queries to extract meaningful insights from it.
**1. Top 5 Most Popular Genres by the Number of Movies:**
**2. Average Rating per Genre:**
**3. Genre Popularity by Decade:**
**4. Most Popular Movies by Votes:**
---

### **Conclusion**

By completing these steps, you will have:

1. Cleaned and transformed the IMDb dataset for analysis.
2. Loaded the data into a PostgreSQL database.
3. Created insightful SQL queries to extract trends and patterns from the data, such as:
    - Popular genres
    - Average ratings by genre
    - Movie popularity trends over the decades

You can extend this project by adding more transformations or visualizing the results using **Tableau**, **Power BI**, or **matplotlib** in Python.

**If you want to stay updated and be part of community, you can join channels below:**
WhatsApp Channel: [https://whatsapp.com/channel/0029Var3a3zFHWqARmaU462V] 
Telegram Channel: [https://t.me/data_land_im_nsk]

❤️Think this is useful? Don't forget to give star (top right corener) 🌟🌟🌟
