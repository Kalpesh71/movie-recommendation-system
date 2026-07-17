import pickle
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

movie_list = movies['title'].values.tolist()


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ccc3ad50dc75c7b838c1234eba33be7b&language=en-US".format(movie_id)
    for attempt in range(3):  # 3 baar try karega
        try:
            data = requests.get(url, timeout=10)
            data = data.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                return "https://via.placeholder.com/500x750?text=No+Image"
        except requests.exceptions.RequestException:
            continue  # fail hua toh phir se try karega
    return "https://via.placeholder.com/500x750?text=No+Image"  # 3 baar fail hone par placeholder

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    selected_movie = None

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        if selected_movie:
            names, posters = recommend(selected_movie)
            recommendations = list(zip(names, posters))

    return render_template(
        'index.html',
        movie_list=movie_list,
        recommendations=recommendations,
        selected_movie=selected_movie
    )


if __name__ == '__main__':
    app.run(debug=True)