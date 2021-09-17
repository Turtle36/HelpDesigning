from app.main import db
from sqlalchemy import INTEGER, String, TEXT, TIME
from sqlalchemy.schema import FetchedValue


class Table(db.Model):
    __tablename__ = 'page'
    name = db.Column(db.String(), primary_key=True)  # Name | String
    content = db.Column(db.String())  # Content | String

    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __repr__(self):
        return '<id {}>'.format(self.name)
