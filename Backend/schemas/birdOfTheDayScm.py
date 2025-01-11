from datetime import datetime
from marshmallow import Schema, fields, validate, validates_schema

seasons = [ 'Spring', 'Summer', 'Fall', 'Winter' ]

class PlainBirdSchema(Schema):
    Id = fields.Integer(dump_only=True)
    Name = fields.String(required = True)
    AdoptedFrom = fields.String(required=False)
    YearPublished = fields.Integer(
                                    required=True,
                                    validate=validate.Range(min=2022, max=datetime.now().year)
                                )
    SeasonCollection = fields.String(required=True, validate=validate.OneOf(seasons))
    HolidayCollection = fields.String(required=False)
    PhotoURL = fields.String(required=False)
    PhotoPublicId = fields.String(required=False)
    PhotoFileName = fields.String(required=False)
    UserId = fields.Integer(dump_only=True)

class PlainBirdOfTheDaySchema(Schema):
    Id = fields.Integer(dump_only=True)
    UserName = fields.String(required = False)
    ChosenDate = fields.DateTime(required=False)
    BirdId = fields.Integer(dump_only=True)

class BirdOfTheDaySchema(PlainBirdOfTheDaySchema):
    bird = fields.Nested(PlainBirdSchema, dump_only=True)