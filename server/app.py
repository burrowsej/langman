""" Server entry point """

"""
flask_restplus is no longer supported. Community has forked to flask_restx 
but this downgrades flask, werkzeug etc. security review needed 
to keep using flask_restplus the following workarounds are needed:
"""
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restplus import Resource, Api, Namespace
from flask import Flask, g
from flask_cors import CORS

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import datetime
import random
import uuid

from .util import get_config
from .langman_orm import Usage, User, Game

"""
The primary advantage of using an API Namespace is that the API can be specified 
first in one file and then added to the app in a different file.
"""
games_api = Namespace('games', description='Creating and playing games')

@games_api.route('')
class Games(Resource):
    valid_langs = ('en', 'es', 'fr')
    def post(self):
        '''Start a new game and return the game id
        
        :route: ``/`` GET
        
        :payload:
            * ``username`` A string containing the player's name
            * ``language`` Language to play in (e.g., 'en')
        
        :returns:
            A success message:
                * ``message`` Literal 'success'
                * ``game_id`` The new game's UUID
        '''
        # check input is valid
        if not (
            games_api.payload and
            'username' in games_api.payload and
            'language' in games_api.payload):
            games_api.abort(400, 'New game POST requires username and language')
        
        lang = games_api.payload['language']
        name = games_api.payload['username']
        user_id = str(uuid.uuid3(uuid.NAMESPACE_URL, name))
        if lang not in self.valid_langs:
            return {
                'message': 'New game POST language must be from ' +
                ', '.join(Games.valid_langs)}, 400
        
        # if user does not exist, create user; get user id
        user = g.games_db.query(User).filter(
            User.user_id==user_id).one_or_none()
        if user is None:
            user = User(
                user_id = user_id,
                user_name = name,
                first_time = datetime.datetime.now(),
            )
            g.games_db.add(user)
            g.games_db.commit()
            user = g.games_db.query(User).filter(
                User.user_name==name).one()
        user._game_started(lang)

        # select a language example
        usage = g.usage_db.query(Usage).filter(
            Usage.language==lang).order_by(func.random()).first()

        # create the new game
        new_game_id = str(uuid.uuid4())
        new_game = Game(
            game_id = new_game_id,
            player = user.user_id,
            usage_id = usage.usage_id,
            bad_guesses = 0,
            reveal_word = '_' * len(usage.secret_word),
            start_time = datetime.datetime.now()
        )
        g.games_db.add(new_game)
        g.games_db.commit()
        return {'message': 'success', 'game_id':new_game_id }



        num_games = g.usage_db.query(Usage).count()
        return {'message': 'under construction - ' + str(num_games) + ' games'}

@games_api.route('/<game_id>')
class OneGame(Resource):
    def get(self, game_id):
        '''Get the state o fthe game'''
        return {'message':'Game GET under construction'}
    
    def put(self, game_id):
        '''Guess a letter and update the game state accordingly'''
        return {'message' 'Game PUT under construction'}
    
    def delete(self, game_id):
        '''End the game, delete the record'''
        return {'message': 'Game DELETE under construction'}


# create the app and configure it
app = Flask(__name__)
app.config.update(get_config(app.config['ENV'],
    app.open_resource('config.yaml')))

@app.before_request
def init_db():
    '''
    Initialise the db by creating the global db_session.

    This gets decorated with @app.before_request to run 
    on each request
    '''
    if not hasattr(g, 'usage_db'):
        db_usage = create_engine(app.config['DB_USAGE'])
        g.usage_db = sessionmaker(db_usage)()
    
    if not hasattr(g, 'games_db'):
        db_games = create_engine(app.config['DB_GAMES'])
        g.games_db = sessionmaker(db_games)()

@app.teardown_request
def close_db(exception):
    '''
    Close down db connection; same one cannot be used between threads.

    This gets decorated with @app.teardown_request to close 
    the db connection after each request
    '''
    if hasattr(g, 'usage_db'):
        g.usage_db.close()
        _ = g.pop('usage_db')
    
    if hasattr(g, 'games_db'):
        g.games_db.close()
        _ = g.pop('games_db')

"""
Cross-origin resource sharing.
This will allow the React client downloaded from one server (e.g., localhost:3000) 
to access the API at a different server (e.g., localhost:5000). Without it, it would 
be very difficult to develop the front-end and back-end together. However, when we 
deploy, we will be able to remove it since the client and the API will be served 
from the same URL.
"""
CORS(app)

# create RESTplus api on app
api = Api(app)
api.add_namespace(games_api, path='/api/games') # insert games namespace
# -- client expects /api/games; changed from/games to /api/games here.

