import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from database.models import setup_db, Movie, Actor
from app import create_app


class CastingTestCase(unittest.TestCase):
    """This class represents the resource test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ['DATABASE_URL']
        self.token = os.environ['ACCESS_TOKEN']
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_actor = {
            'name': 'Vin Diesel',
            'age': 52,
            'gender': 'M'
        }

        self.new_movie = {
            'title': 'F9: The Fast Saga',
            'release_date': '02/04/2021'
        }

        self.update_actor = {
            'age': 53
        }

        self.update_movie = {
            'release_date': '03/04/2021'
        }

        self.auth = {
            "Authorization": self.token
        }

        self.invalid_auth = {
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImFucUh0cm5PZ254UDZjMURVNkVPaiJ9.eyJpc3MiOiJodHRwczovL3JhamZzbmQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlY2E0NDFmZWU1NmM0MGM2ZDgzYzAyMSIsImF1ZCI6IkNhcGVBdXRoIiwiaWF0IjoxNTkwNTA4NzcyLCJleHAiOjE1OTA1OTUxNzIsImF6cCI6IkRuSUZ0NW0zMmk0SHZzQndlZ0VNMjJjYVNxcERWMUFjIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Y2Fwc3RvbmUiXX0.M75gvpb-XVFKNHkstmrr9d6U2BlXL3rfpqzqroB39-P281WXcVCQntQnreimCYuJf0OxtXknR3J-lCvKwY2afb2gVtLhYgMSC16gcrGwuCbePku6EGfiy1jobT5AoVEH4obYLqVQzsOz7dspA3aVBRKhjLfBXAw2PWT_tWlPPvzewL2aVEZLZ_KhMNxPru2iFb8jNi4lXncK5WGA25J0530rhMm9vAsqaF5JQPXiM_ZVy1TXmO0kIv2Wd_HJZqcITHdmgCnuUMIwjmQ_5dKjvi_-6yvwJeED-ifQot-lBDoyikbQ7-OZxGc3UjJbrl65_fksQH8OIRaUvztNZpWLZQ"
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    def test_1_get_welcome(self):

        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['Message']))

    def test_2_create_actor(self):

        res = self.client().post('/actors', json=self.new_actor, headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_3_create_movie(self):

        res = self.client().post('/movies', json=self.new_movie, headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_4_get_actors(self):

        res = self.client().get('/actors', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_5_get_movies(self):

        res = self.client().get('/movies', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_6_get_actor_by_id(self):

        res = self.client().get('/actors/1', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actor']))

    def test_7_get_movie_by_id(self):

        res = self.client().get('/movies/1', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movie']))

    def test_8_update_actor(self):

        res = self.client().patch('/actors/1', json=self.update_actor, headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_9_update_movie(self):

        res = self.client().patch('/movies/1', json=self.update_movie, headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_E1_404_get_actor_by_id(self):

        res = self.client().get('/actors/50', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_E2_404_get_movie_by_id(self):

        res = self.client().get('/movies/50', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_E3_422_create_actor_unprocessable(self):

        res = self.client().post('/actors', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'unprocessable')

    def test_E4_422_create_movie_unprocessable(self):

        res = self.client().post('/movies', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'unprocessable')

    def test_E5_404_update_actor(self):

        res = self.client().patch('/actors/100', json=self.update_actor, headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_E6_404_update_movie(self):

        res = self.client().patch('/movies/100', json=self.update_movie, headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_E7_404_delete_actor(self):

        res = self.client().delete('/actors/100', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_E8_404_delete_movie(self):

        res = self.client().delete('/movies/100', headers=self.auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'], 'Resource Not Found')

    def test_E9_401_auth_missing(self):

        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')

    def test_E10_403_unauthorized(self):

        res = self.client().post('/movies', json=self.new_movie, headers=self.invalid_auth)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')

    def test_Z_delete_actor(self):

        res = self.client().delete('/actors/1', headers=self.auth)
        data = json.loads(res.data)

        actor = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(actor, None)

    def test_Z_delete_movie(self):

        res = self.client().delete('/movies/1', headers=self.auth)
        data = json.loads(res.data)

        movie = Movie.query.filter(Movie.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(movie, None)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
