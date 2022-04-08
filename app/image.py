from app.main import app
from flask import url_for, redirect


@app.route("/image/icon.png")
def icon_png():
    return redirect(url_for("static", filename='img/png/icon.png'))


@app.route("/image/rocket.png")
def rocket_png():
    return redirect(url_for("static", filename='img/png/rocket.png'))


@app.route("/image/picture.png")
def picture_png():
    return redirect(url_for("static", filename='img/png/picture.png'))


@app.route("/image/paint.png")
def paint_png():
    return redirect(url_for("static", filename='img/png/paint.png'))


@app.route("/image/icon.ico")
def icon_ico():
    return redirect(url_for("static", filename='img/ico/icon.ico'))


@app.route("/image/star_full.svg")
def start_full_svg():
    return redirect(url_for("static", filename='img/svg/star_full.svg'))


@app.route("/image/empty_star.svg")
def empty_star_svg():
    return redirect(url_for("static", filename='img/svg/empty_star.svg'))


@app.route("/image/user.png")
def user_png():
    return redirect(url_for("static", filename='img/png/user.png'))


@app.route("/image/bubling.jpg")
def photounyup_jpg():
    return redirect(url_for("static", filename='img/jpg/bubling.jpg'))