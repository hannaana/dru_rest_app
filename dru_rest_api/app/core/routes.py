from flask import Flask, request
from flask import current_app as app

from app.controllers.actor import *
from app.controllers.movie import *


@app.route('/api/actors', methods=['GET'])
def actors():
    """
    Get all actors in db
    """
    return get_all_actors()

@app.route('/api/movies', methods=['GET'])
def movies():
    """
    Get all actors in db
    """
    return get_all_movies()


@app.route('/api/actor', methods=['GET', 'POST', 'PUT', 'DELETE'])
def actor():
    if request.method == 'GET':
        return get_actor_by_id()
    elif request.method == 'POST':
        return add_actor()
    elif request.method == 'PUT':
        return update_actor()
    else:
        return delete_actor()

@app.route('/api/movie', methods=['GET', 'POST', 'PUT', 'DELETE'])
def movie():
    if request.method == 'GET':
        return get_movie_by_id()
    elif request.method == 'POST':
        return add_movie()
    elif request.method == 'PUT':
        return update_movie()
    else:
        return delete_movie()


@app.route('/api/actor_relations', methods=['PUT', 'DELETE'])
def actor_relations():
    if request.method == 'PUT':
        return actor_add_relation()
    else:
        return actor_clear_relations()


@app.route('/api/movie_relations', methods=['PUT', 'DELETE'])
def movie_relations():
    if request.method == 'PUT':
        return movie_add_relation()
    else:
        return movie_clear_relations()




"""
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

"""