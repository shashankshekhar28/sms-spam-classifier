🎬 Movie Recommendation System (Content-Based)

A content-based movie recommendation system built using Python, Machine Learning, and Streamlit.
The app recommends movies similar to the one selected by the user based on content similarity and displays movie posters using the TMDB API.

🚀 Features

Content-based movie recommendations

Uses cosine similarity on movie metadata

Interactive UI built with Streamlit

Fetches real-time movie posters using TMDB API

Fast recommendations using precomputed similarity matrix

🛠️ Tech Stack

Python

Pandas

Scikit-learn

Streamlit

Pickle

TMDB API

📂 Project Structure
├── app.py                         # Streamlit web app
├── movie recommender system.ipynb # Model training & preprocessing
├── movies.pkl                     # Processed movie data
├── similarity.pkl                 # Cosine similarity matrix
├── tmdb_5000_movies.csv           # Dataset
├── requirements.txt               # Dependencies
└── README.md                      # Project documentation

⚙️ How It Works

Movie metadata is processed (genres, keywords, cast, crew, overview)

Text data is vectorized

Cosine similarity is calculated between movies

Top 5 similar movies are recommended

Posters are fetched using TMDB API

▶️ How to Run the Project Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run app.py

🔑 TMDB API Key

This project uses the TMDB API to fetch movie posters.

Get your API key from: https://www.themoviedb.org/

Replace the API key in app.py if needed:

https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY

📸 App Preview

Select a movie from the dropdown

Click Recommend

View 5 similar movies with posters

📌 Future Improvements

Add hybrid (content + collaborative) filtering

Improve UI styling

Add search functionality

Deploy on Streamlit Cloud

🧑‍💻 Author

Shashank Shekhar
Machine Learning & Data Science Enthusiast
