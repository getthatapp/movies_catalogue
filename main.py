import random
from flask import Flask, render_template, request
import tmdb_client

app = Flask(__name__)


@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', default='popular')
    valid_lists = ['popular', 'top_rated', 'upcoming', 'now_playing']

    if selected_list not in valid_lists:
        selected_list = 'popular'

    movies = tmdb_client.get_movies(how_many=8, list_type=selected_list)
    return render_template("homepage.html", movies=movies, current_list=selected_list, valid_lists=valid_lists)


@app.route('/movie/<movie_id>')
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    if not details:
        return "Error: Movie not found", 404
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template('movie_details.html', movie=details, cast=cast, selected_backdrop=selected_backdrop)


@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        url = tmdb_client.get_poster_url(path, size)
        print(url)
        return url

    return {"tmdb_image_url": tmdb_image_url}


if __name__ == "__main__":
    app.run(debug=True)
