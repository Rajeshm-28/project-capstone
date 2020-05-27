import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from sqlalchemy import exc

from database.models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    # cors
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, DELETE, PATCH')
        return response

    @app.route("/", methods=['GET'])
    def welcome(*args, **kwargs):
        try:
            return jsonify({
                'success': True,
                'Message': 'Welcome To Casting Agency'
            })

        except AttributeError:
            abort(422)

    # Return all movies
    @app.route("/movies")
    @requires_auth('get:capstone')
    def get_movies(*args, **kwargs):
        try:
            all_movies = Movie.query.order_by(Movie.id).all()
            movies = [d.format() for d in all_movies]

            if len(all_movies) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'movies': movies
            })

        except AttributeError:
            abort(422)

    # Return movie by id
    @app.route("/movies/<int:movie_id>", methods=['GET'])
    @requires_auth('get:capstone')
    def get_movie(*args, **kwargs):

        M_id = kwargs['movie_id']

        try:
            movie = Movie.query.filter(Movie.id == M_id).one_or_none()

            if movie is None:
                abort(404)

            return jsonify({
                'success': True,
                'movie': movie.format()
            })

        except AttributeError:
            abort(422)

    # Return all the actors
    @app.route("/actors")
    @requires_auth('get:capstone')
    def get_actors(*args, **kwargs):
        try:
            all_actors = Actor.query.order_by(Actor.id).all()
            actors = [d.format() for d in all_actors]

            if len(all_actors) == 0:
                abort(404)

            return jsonify({
                'success': True,
                'actors': actors
            })

        except AttributeError:
            abort(422)

    # Return actor by ID
    @app.route("/actors/<int:actor_id>", methods=['GET'])
    @requires_auth('get:capstone')
    def get_actor(*args, **kwargs):

        A_id = kwargs['actor_id']

        try:
            actor = Actor.query.filter(Actor.id == A_id).one_or_none()

            if actor is None:
                abort(404)

            return jsonify({
                'success': True,
                'actor': actor.format()
            })

        except AttributeError:
            abort(422)

    # Insert Movie
    @app.route("/movies", methods=['POST'])
    @requires_auth('post:movie')
    def create_movies(*args, **kwargs):
        try:
            body = request.get_json()
            new_title = body.get('title')
            new_release_date = body.get('release_date')

            movie = Movie(title=new_title, release_date=new_release_date)
            movie.insert()

            return jsonify({
                'success': True,
                "message": "Movie Successfully Added!",
                "movies": movie.format()
            })

        except AttributeError:
            abort(422)

    # Insert actor
    @app.route("/actors", methods=['POST'])
    @requires_auth('post:actor')
    def create_actors(*args, **kwargs):
        try:
            body = request.get_json()
            new_name = body.get('name')
            new_age = body.get('age')
            new_gender = body.get('gender')

            actor = Actor(name=new_name, age=new_age, gender=new_gender)
            actor.insert()

            return jsonify({
                'success': True,
                "message": "Actor Successfully Added!",
                "actor": actor.format()
            })

        except AttributeError:
            abort(422)

    # Update Movie
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:capstone')
    def update_movie(*args, **kwargs):

        M_id = kwargs['movie_id']

        try:
            movie = Movie.query.filter(Movie.id == M_id).one_or_none()

            if movie is None:
                abort(404)

            body = request.get_json()

            new_title = body.get('title', None)
            new_release_date = body.get('release_date', None)

            if new_title is not None:
                movie.title = new_title

            if new_release_date is not None:
                movie.release_date = new_release_date

            movie.update()

            return jsonify({
                "success": True,
                "message": "Movie successfully updated!",
                "movie": [movie.format()]
            })

        except AttributeError:
            abort(422)

    # Update Actor
    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:capstone')
    def update_actor(*args, **kwargs):

        A_id = kwargs['actor_id']

        try:
            actor = Actor.query.filter(Actor.id == A_id).one_or_none()

            if actor is None:
                abort(404)

            body = request.get_json()

            new_name = body.get('name', None)
            new_age = body.get('age', None)
            new_gender = body.get('gender', None)

            if new_name is not None:
                actor.name = new_name

            if new_age is not None:
                actor.age = new_age

            if new_gender is not None:
                actor.gender = new_gender

            actor.update()

            return jsonify({
                "success": True,
                "message": "Actor successfully updated!",
                "actor": [actor.format()]
            })

        except AttributeError:
            abort(422)

    # Delete movie
    @app.route("/movies/<int:movie_id>", methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(*args, **kwargs):

        M_id = kwargs['movie_id']

        try:
            movie = Movie.query.filter(Movie.id == M_id).one_or_none()

            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'message': "Movie successfully deleted!"
            })

        except AttributeError:
            abort(422)

    # Delete Actor
    @app.route("/actors/<int:actor_id>", methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(*args, **kwargs):

        A_id = kwargs['actor_id']

        try:
            actor = Actor.query.filter(Actor.id == A_id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'message': "Actor successfully deleted!"
            })

        except AttributeError:
            abort(422)

    # Error Handling
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False,
                        "error": 422,
                        "message": "unprocessable"
                        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        })

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized'
        })

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'forbidden'
        })

    @app.errorhandler(405)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        })

    @app.errorhandler(AuthError)
    def error_auth(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)