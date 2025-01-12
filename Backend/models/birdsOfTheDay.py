import pytz
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from flask_smorest import abort
from datetime import datetime
from db import db
from models.birds import BirdsModel
from models.user import UsersModel

class BirdsOfTheDayModel(db.Model):
    __tablename__ = 'BirdsOfTheDay'

    Id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String, nullable=True)
    ChosenDate = db.Column(db.DateTime, nullable=False)

    # Relationships
    BirdId = db.Column(db.Integer, db.ForeignKey('Birds.Id'), nullable=False)
    bird = db.relationship('BirdsModel', back_populates='birdOfTheDay')

    @classmethod
    def choose_new_bird(cls):
        chosen_bird = db.session.query(BirdsModel, UsersModel)\
                        .join(UsersModel, UsersModel.Id == BirdsModel.UserId)\
                        .order_by(func.random())\
                        .first()

        bird, user = chosen_bird

        new_bird = cls(
            UserName = user.Username,
            ChosenDate = datetime.now(pytz.UTC),
            BirdId = bird.Id
        )

        try:
            db.session.add(new_bird)
            db.session.commit()
        except SQLAlchemyError as error:
            db.session.rollback()
            abort(500, message = str(error))

        return new_bird

    def __repr__(self):
        return f'''
            <
                \n id: {self.Id}
                \n name: {self.UserName}
                \n chosen_date: {self.ChosenDate}
                \n bird_id: {self.BirdId}
        '''