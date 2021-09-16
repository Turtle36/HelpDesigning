import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/S3Kf028Dk3kdSa3dkdkKFJA488(!839kdk:1!/fkKAKejsja")
# mengambil header dari objek request
def headers():
    headers = request.headers
    response = ['%s = %s' % (key, value) \
                for key, value in sorted(headers.items())
                ]
    response = '<br/>'.join(response)
    return response


from app.views import *
