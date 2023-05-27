import requests
import config


def get_movies_list(list_type='popular'):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    api_key = config.API_KEY
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occured: {err}")
        return {}
    except Exception as err:
        print(f"An error occured: {err}")
        return {}

    return call_tmdb_api(f"movie/{list_type}")


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_key = config.API_KEY
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occured: {err}")
        return {}
    except Exception as err:
        print(f"An error occured: {err}")
        return {}

    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_key = config.API_KEY
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    api_key = config.API_KEY
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type="popular"):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    api_key = config.API_KEY
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()