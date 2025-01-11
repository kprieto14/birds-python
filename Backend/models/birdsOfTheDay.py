from db import db

class BirdsOfTheDayModel(db.Model):
    __tablename__ = 'BirdsOfTheDay'

    Id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String, nullable=True)
    ChosenDate = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    # Relationships
    BirdId = db.Column(db.Integer, db.ForeignKey('User.Id'), nullable=False)
    bird = db.relationship('UsersModel', back_populates='birdOfTheDay')

    def __repr__(self):
        return f'''
            <
                \n id: {self.Id}
                \n name: {self.UserName}
                \n chosen_date: {self.ChosenDate}
                \n bird_id: {self.BirdId}
        '''