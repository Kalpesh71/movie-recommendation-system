# 🎬 CineMatch AI – Intelligent Movie Recommendation System

**An AI-powered Movie Recommendation Platform that uses Machine Learning to recommend similar movies based on content similarity.**

---

# 📌 Overview

**CineMatch AI** is a **Final Year Computer Science Engineering Project** developed using **Machine Learning, Flask, HTML, CSS, and JavaScript**.

The platform recommends movies based on their content by analyzing features such as genres, cast, crew, keywords, and movie overview. It uses a **Content-Based Recommendation System** with **Cosine Similarity** to find movies that are most similar to the user's selected movie.

Users simply search for a movie, and the system instantly provides a list of similar movies.

This project demonstrates the practical implementation of Machine Learning in building an intelligent recommendation system with a responsive web interface.

---

# 🎯 Objectives

- Build an intelligent Movie Recommendation System.
- Implement a Content-Based Recommendation Algorithm.
- Recommend similar movies based on user input.
- Develop a responsive web application using Flask.
- Demonstrate Machine Learning concepts in a real-world application.
- Improve user experience for movie discovery.

---

# 🚀 Key Features

## 🎥 Movie Recommendation

- Search any movie
- Get Top Recommended Movies
- Content-Based Recommendation
- Fast Recommendation Engine

---

## 🤖 Machine Learning Module

Uses Machine Learning techniques for

- Data Cleaning
- Feature Engineering
- Text Preprocessing
- Vectorization
- Similarity Calculation
- Recommendation Generation

---

## 🧠 Recommendation Engine

The recommendation engine analyzes

- Genres
- Cast
- Director
- Keywords
- Movie Overview

and recommends the most similar movies using cosine similarity.

---

## 🌐 Web Application

Built using Flask Framework

Features

- Responsive Interface
- Search Functionality
- Dynamic Recommendations
- Fast Performance
- Easy Navigation

---

## 📊 Dataset

Uses the **TMDB 5000 Movie Dataset**

Dataset includes

- Movie ID
- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview

Total Movies

**4800+ Movies**

---

# 🏗 System Architecture

```
                   User
                     │
                     ▼
          HTML + CSS + JavaScript
                     │
                     ▼
               Flask Backend
                     │
        ┌────────────┼─────────────┐
        │                          │
        ▼                          ▼
 Machine Learning Model      TMDB Dataset
        │                          │
        └────────────┼─────────────┘
                     ▼
         Movie Recommendation Result
```

---

# 🔄 Workflow

```
User Opens Website
        │
Search Movie
        │
Receive Movie Name
        │
Data Preprocessing
        │
Feature Extraction
        │
Count Vectorization
        │
Cosine Similarity
        │
Recommend Similar Movies
        │
Display Results
```

---

# 🧠 Machine Learning

### Algorithm Used

- Content-Based Recommendation System

### Vectorization

- CountVectorizer

### Similarity Technique

- Cosine Similarity

### Responsibilities

- Data Cleaning
- Feature Engineering
- Text Processing
- Movie Recommendation

---

# 📂 Dataset Information

Dataset Used

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

Important Features

- movie_id
- title
- genres
- keywords
- cast
- crew
- overview

---

# 💻 Technology Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- Flask

## Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- NLTK

## Dataset

- TMDB 5000 Dataset

---

# 📂 Project Structure

```
Movie-Recommendation-System/

│── app.py
│── recommendation.py
│── model.py
│── requirements.txt
│── README.md

├── dataset/
│     ├── tmdb_5000_movies.csv
│     └── tmdb_5000_credits.csv
│
├── models/
│     ├── movie_dict.pkl
│     └── similarity.pkl
│
├── static/
│     ├── css/
│     ├── js/
│     └── images/
│
├── templates/
│     └── index.html
│
├── notebooks/
│     └── Movie Recommendation.ipynb
│
└── utils/
```

---

# ⚙ Installation

Clone Repository

```bash
git clone https://github.com/YourUsername/Movie-Recommendation-System.git
```

Go to Project Folder

```bash
cd Movie-Recommendation-System
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Flask Server

```bash
python app.py
```

Open Browser

```
http://127.0.0.1:5000
```

---

# 🌟 Future Enhancements

- User Login System
- Favorite Movies
- Movie Posters using TMDB API
- IMDb Ratings
- Genre Filtering
- Personalized Recommendations
- Search History
- Responsive UI Improvements
- Cloud Deployment

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of

- Machine Learning
- Recommendation Systems
- Natural Language Processing
- Feature Engineering
- Data Preprocessing
- Cosine Similarity
- Flask Web Development
- Frontend Development
- Full Stack Development

---

# 👨‍💻 Developed By

**Kalpesh Saini**

Bachelor of Technology (Computer Science Engineering)

**Final Year Project**

---

If you found this project useful, please give it a ⭐ on GitHub.