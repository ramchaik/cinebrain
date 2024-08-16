# 🎬 CineBrain: Movie Recommender System

CineBrain is an intelligent movie recommender system that suggests similar movies based on user selection. It utilizes the TMDB 5000 Movie Dataset and employs advanced natural language processing techniques to provide accurate recommendations.

## 🚀 Demo

https://github.com/user-attachments/assets/0a67e42f-faa6-4059-9cc0-a00dcebe53fb

## 📚 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Model Architecture](#-model-architecture)
- [Key Features](#-key-features)
- [Directory Structure](#-directory-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technologies Used](#-technologies-used)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [License](#-license)

## 🌟 Project Overview

CineBrain is designed to enhance the movie discovery experience by leveraging machine learning and natural language processing techniques. The system analyzes various aspects of movies, including overview, cast, crew, genres, and keywords, to generate meaningful recommendations.

## 📊 Dataset

The project uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle, which includes metadata on approximately 5,000 movies from The Movie Database (TMDb).

## 🧠 Model Architecture

The recommendation model follows these key steps:

1. **Data Loading and Preprocessing:**
   - Load the dataset into a pandas DataFrame
   - Handle missing values and drop null entries
   - Convert JSON strings to tags for cast and crew information

2. **Feature Engineering:**
   - Tokenize movie overviews
   - Create a cumulative tag for each movie, combining information from overview, crew, cast, genres, and keywords

3. **Vectorization:**
   - Utilize CountVectorizer from scikit-learn
   - Set dimension size to 5000 and remove English stop words
   - Apply stemming using PorterStemmer from NLTK to reduce word duplications

4. **Similarity Calculation:**
   - Compute cosine similarity between movie vectors

5. **Recommendation Generation:**
   - Implement a recommendation method that calculates cosine similarity between the selected movie and all other movies in the dataset
   - Return the top 5 movies with the highest similarity scores

## ✨ Key Features

- Select a movie from the list to receive top 5 movie recommendations
- User-friendly interface built with Flask, HTMX, and Tailwind CSS
- Efficient data processing and similarity calculation for quick recommendations

## 📁 Directory Structure

```sh
cinebrain/
│
├── app/                # Flask application directory
│
├── data/               # Data directory
│   ├── processed_df.pkl
│   ├── tmdb_5000_credits.csv
│   ├── tmdb_5000_movies.csv
│   └── similarity.npy
│
├── recommender_system.ipynb  # Jupyter notebook for model development
├── run.py                    # Script to run the Flask application
├── .env                      # Environment file for API key
└── README.md
```

## 🔑 API Setup

This project uses The Movie Database (TMDb) API to fetch additional movie information. To use the API:

1. Create an account on [The Movie Database](https://www.themoviedb.org/)
2. Go to your account settings and navigate to the API section
3. Request an API key for developer use
4. Create a `.env` file in the root directory and add your key:

```sh
TMDB_API_KEY=your_api_key_here
```

⚠️ Keep your API key confidential and never share it publicly.

## 🛠️ Installation

1. Clone the repository:

```sh
git clone https://github.com/ramchaik/cinebrain.git
cd cinebrain
```

2. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## 🖥️ Usage

1. Run the Flask application:

```sh
python run.py
```

2. Open a web browser and navigate to `http://localhost:5000`

3. Select a movie from the list to receive recommendations

## 🛠️ Technologies Used

- Python
- pandas
- scikit-learn
- NLTK
- Flask
- HTMX
- Tailwind CSS

## 🔮 Future Improvements

- Implement user authentication and personalized recommendations
- Integrate real-time data updates from TMDb API
- Enhance the user interface with movie posters and additional details
- Develop a mobile application for on-the-go recommendations

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).