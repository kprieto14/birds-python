from datetime import date
from db import db
from flask import request
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.birdsOfTheDay import BirdsOfTheDayModel
from schemas.birdOfTheDayScm import BirdOfTheDaySchema

blueprint = Blueprint('BirdOfTheDay', __name__, description='Operations to GET the Bird of the Day for home page')

@blueprint.route('/api/birdOfTheDay')
class BirdOfTheDay(MethodView):
    @blueprint.response(200, BirdOfTheDaySchema)
    def get(self):
        """Get the bird of the day, if it is out of date, make a new one"""
        bird_of_day = db.session.query(BirdsOfTheDayModel)\
                        .filter(BirdsOfTheDayModel.ChosenDate == date.today())\
                        .first()

        if bird_of_day == None:
            bird_of_day = BirdsOfTheDayModel.choose_new_bird()

        return bird_of_day