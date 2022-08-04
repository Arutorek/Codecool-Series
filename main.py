from flask import Flask, render_template, url_for, request, jsonify
from data import queries
import math
from dotenv import load_dotenv
import utils
from util import json_response


load_dotenv()
app = Flask('codecool_series')

@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/shows')
@app.route('/shows/<int:page>')
@app.route('/shows/most-rated')
@app.route('/shows/most-rated/<int:page>')
def most_rated(page=1):
    order_by, order_direction = 'rating', 'desc'
    if request.args:
        order_by = list(dict(request.args).keys())[0]
        order_direction = dict(request.args)[order_by]
    number_of_shows = queries.get_show_count()[0]['show_count']
    page_count = math.ceil(number_of_shows/15)
    shown_pages = utils.check_pages(page, page_count)
    most_rated_shows = queries.get_most_rated_shows(page, order_by, order_direction)
    get_rated_shows(most_rated_shows)
    return render_template('most-rated.html', shows=most_rated_shows,
                           shown_pages=shown_pages, page_count=page_count,
                           page=page, url=request.url, order_by=order_by,
                           order_direction=order_direction)


def get_rated_shows(most_rated_shows):
    for show in most_rated_shows:
        genres = []
        show_id = show['id']
        get_genres = queries.get_genres_from_show(show_id)
        for genre in get_genres:
            genres.append(genre['name'])
        show['genres'] = genres
    return most_rated_shows


@app.route('/show/<id>')
def show_details(id):
    show_data = queries.get_show_data(id)[0]
    show_genres = queries.get_genres_from_show(id)
    show_actors = queries.get_show_actors(id)
    seasons = queries.get_seasons(id)
    return render_template('show-details.html', show_data=show_data, show_actors=show_actors,
                           show_genres=show_genres, seasons=seasons)


@app.route('/actors')
def actors():
    get_actors = queries.get_100_actors()
    return render_template('actors-list.html', actors=get_actors)


@app.route('/api/actor-shows/<int:actor_id>/')
@json_response
def get_shows_by_actor_id(actor_id):
    return queries.get_show_id_by_actor(actor_id)


@app.route('/api/get-characters/<character_id>')
@json_response
def get_characters(character_id):
    test = queries.get_actor(character_id)
    name = test[0]['name']
    birthday = str(test[0]['birthday'])
    return (name, birthday)


@app.route('/genres')
def genres():
    genres_data = queries.get_genres()
    return render_template('pa.html',genres_data=genres_data)


@app.route('/api/get-series/<int:data_id>')
@json_response
def get_shows_by_genre(data_id):
    return queries.get_shows_genre(data_id)


def main():
    app.run(debug=False)


if __name__ == '__main__':
    main()
