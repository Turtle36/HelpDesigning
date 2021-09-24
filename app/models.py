from app.main import db
from sqlalchemy import INTEGER, String, TEXT, TIME
from sqlalchemy.schema import FetchedValue


class User(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    class SignUp(object):
        def __init__(self, username=None, password=None):
            self.username = username
            self.password = password

        def setUsername(self, username):
            self.username = username

        def getUsername(self):
            return self.username

        def setPassword(self, password):
            self.password = password

        def getPassword(self):
            return self.password

    class Login(object):
        def __init__(self, username=None, password=None):
            self.username = username
            self.password = password

        def setUsername(self, username):
            self.username = username

        def getUsername(self):
            return self.username

        def setPassword(self, password):
            self.password = password

        def getPassword(self):
            return self.password


class article(db.Model):
    __tablename__ = 'article'
    name = db.Column(String(), primary_key=True)  # Name | String
    content = db.Column(String())  # Content | String
    user = db.Column(String())  # User | String

    def __init__(self, name, content, user):
        self.name = name
        self.content = content
        self.user = user

    def __repr__(self):
        return '<id {}>'.format(self.name)


class sign_up(db.Model):
    __tablename__ = 'sign_up'
    id = db.Column(INTEGER(), primary_key=True)  # ID | Integer
    username = db.Column(String(), unique=True)  # Username | String
    password = db.Column(String())  # Password | String

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)


class login(db.Model):
    __tablename__ = 'login'
    id = db.Column(INTEGER(), primary_key=True)  # ID | Integer
    username = db.Column(String())  # Username | String
    password = db.Column(String())  # Password | String

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
