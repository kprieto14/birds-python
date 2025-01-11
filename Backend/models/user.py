from db import db

class UsersModel(db.Model):
    __tablename__ = 'Users'

    Id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String, nullable=False)
    HashedPassword = db.Column(db.String, nullable=True)
    Username = db.Column(db.String, nullable=False)

    # Relationships
    birds = db.relationship('BirdsModel', back_populates='user', lazy='dynamic', cascade='all, delete')

    def __repr__(self):
        return f'''
            <
                \n id: {self.Id}
                \n email: {self.Email}
                \n user_name: {self.Username}
            >
        '''