from flask import jsonify, make_response

from datetime import datetime as dt
from ast import literal_eval

from app.models.movie import Movie
from app.models.actor import Actor
from app.settings.constants import ACTOR_FIELDS  # to make response pretty
from app.controllers.parse_request import get_request_data


def get_all_actors():
    """
    Get list of all records
    """
    all_actors = Actor.query.all()
    actors = []
    for actor in all_actors:
        act = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        actors.append(act)
    return make_response(jsonify(actors), 200)


def get_actor_by_id():
    """
    Get record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Actor.query.filter_by(id=row_id).first()
        try:
            actor = {k: v for k, v in obj.__dict__.items() if k in ACTOR_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def add_actor():
    """
    Add new actor
    """
    data = get_request_data()
    ### YOUR CODE HERE ###

    # use this for 200 response code
    #new_record = Actor(form.rssfeed.data)
    new_record = Actor.create(**data)
    #new_record = Actor(Actor.name=data['name'], )
    # db.add(new_record)
    # db.commit()
    new_actor = {k: v for k, v in new_record.__dict__.items() if k in ACTOR_FIELDS}
    return make_response(jsonify(new_actor), 200)
    ### END CODE HERE ###


def update_actor():
    """
    Update actor record by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    try:
        row_id = int(data['id'])
    except:
        err = 'Id must be integer'
        return make_response(jsonify(error=err), 400)

    # use this for 200 response code
    upd_record = Actor.query.filter_by(id=row_id).first().update(row_id, **data)
    upd_actor = {k: v for k, v in upd_record.__dict__.items() if k in ACTOR_FIELDS}
    return make_response(jsonify(upd_actor), 200)
    ### END CODE HERE ###


def delete_actor():
    """
    Delete actor by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    try:
        row_id = int(data['id'])
    except:
        err = 'Id must be integer'
        return make_response(jsonify(error=err), 400)

    # Actor.query.filter_by(id=row_id).delete()
    Actor.delete(row_id)
    # use this for 200 response code
    msg = 'Record successfully deleted'
    return make_response(jsonify(message=msg), 200)
    ### END CODE HERE ###


def actor_add_relation():
    """
    Add a movie to actor's filmography
    """
    # {"id": 23, "relation_id": 2}
    data = get_request_data()
    ### YOUR CODE HERE ###
    try:
        row_id = int(data['id'])
        movie_id = int(data['relation_id'])
    except Exception as err:
        # err = 'Id must be integer'
        return make_response(jsonify(error=err), 400)

    obj = Movie.query.filter_by(id=movie_id).first()

    # use this for 200 response code
    actor = Actor.add_relation(row_id, obj)# add relation here
    rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
    rel_actor['filmography'] = str(actor.filmography)
    return make_response(jsonify(rel_actor), 200)
    ### END CODE HERE ###


def actor_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    ### YOUR CODE HERE ###
    try:
        row_id = int(data['id'])
    except Exception as err:
        # err = 'Id must be integer'
        return make_response(jsonify(error=err), 400)

    # use this for 200 response code
    actor = Actor.clear_relations(row_id) # clear relations here
    rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
    rel_actor['filmography'] = str(actor.filmography)
    return make_response(jsonify(rel_actor), 200)
    ### END CODE HERE ###


if __name__ == "__main__":
    data = {'name': "test1", "gender":"test2", "date_of_birth":"test3"}