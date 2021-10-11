from app.main import app
from flask import url_for, redirect


@app.route("/image/icon.png")
def icon_png():
    return redirect(url_for("static", filename='img/icon.png'))


@app.route("/image/gold.png")
def gold_png():
    return redirect(url_for("static", filename='img/gold.png'))

