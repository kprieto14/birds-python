from db import db

class BirdsModel(db.Model):
    __tablename__ = 'Birds'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    AdoptedFrom = db.Column(db.String, nullable=True)
    YearPublished = db.Column(db.Integer, nullable=False)
    SeasonCollection = db.Column(db.String, nullable=False)
    HolidayCollection = db.Column(db.String, nullable=True)
    PhotoUrl = db.Column(db.String, nullable=True)
    PhotoPublicId = db.Column(db.String, nullable=True)
    PhotoFileName = db.Column(db.String, nullable=True)

    # Relationships
    UserId = db.Column(db.Integer, db.ForeignKey('User.Id'), nullable=False)
    user = db.relationship('UsersModel', back_populates='birds')

    birdOfTheDay = db.relationship( 'BirdsOfTheDayModel', back_populates='bird', use_list=False, cascade='all, delete')

    def __repr__(self):
        return f'''
            <
                \n id: {self.Id}
                \n name: {self.Name}
                \n adopted_from: {self.AdoptedFrom}
                \n year_published: {self.YearPublished}
                \n season_collection: {self.SeasonCollection}
                \n holiday_collection: {self.HolidayCollection}
                \n photo_url: {self.PhotoUrl}
                \n photo_public_id: {self.PhotoPublicId}
                \n photo_file_name: {self.PhotoFileName}
            >
        '''