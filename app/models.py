from app.main import db
from sqlalchemy import INTEGER, String, TEXT, TIME
from sqlalchemy.schema import FetchedValue


class Article(db.Model):
    __tablename__ = 'article'
    name = db.Column(db.String(), primary_key=True)  # Name | String
    content = db.Column(db.String())  # Content | String

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __repr__(self):
        return '<id {}>'.format(self.name)
