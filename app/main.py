import os

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/admin", methods=['GET', 'POST'])
# mengambil header dari objek request
def admin():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        if username == "@boing#admin":
            if password == "#F@boing1234!!Admin":
                headers = request.headers
                response = ['%s = %s' % (key, value) \
                            for key, value in sorted(headers.items())
                            ]
                response = '<br/>'.join(response)
                return response
            else:
                return redirect("/login")
        else:
            return redirect("/login")

    return render_template("admin/login.html")


from app.views import *
