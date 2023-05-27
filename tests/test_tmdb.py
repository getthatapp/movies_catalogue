from unittest.mock import Mock
from movies_catalogue import tmdb_client


def test_get_single_movie(monkeypatch):
    mock_single_movie = {'movie_id': 1, 'title': 'Test Movie', 'overwiev': 'Test Overwiev'}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.status_code = 200
    response.json.return_value = mock_single_movie
    monkeypatch.setattr('requests.get', requests_mock)

    single_movie = tmdb_client.get_single_movie(1)

    assert single_movie == mock_single_movie


def test_get_movie_images(monkeypatch):
    mock_images = {'backdrops': [], 'posters': []}
    requests_mock = Mock()
    response = requests_mock.return_value
    response.status_code = 200
    response.json.return_value = mock_images
    monkeypatch.setattr('requests.get', requests_mock)

    movie_images = tmdb_client.get_movie_images(1)

    assert movie_images == mock_images


def test_get_single_movie_cast(monkeypatch):
    mock_cast = [{'cast_id': 1, 'character': 'Test Character', 'name': 'Test Actor'}]
    requests_mock = Mock()
    response = requests_mock.return_value
    response.status_code = 200
    response.json.return_value = {'cast': mock_cast}
    monkeypatch.setattr('requests.get', requests_mock)

    movie_cast = tmdb_client.get_single_movie_cast(1)

    assert movie_cast == mock_cast