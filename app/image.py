from app.main import app
from flask import url_for, redirect


@app.route("/image/icon.png")
def icon():
    return redirect(url_for("static", filename='image/icon.png'))


@app.route("/image/error.png")
def error_png():
    return redirect(url_for("static", filename='image/error.png'))


@app.route("/image/increase_business.png")
def increase_business_png():
    return redirect(url_for("static", filename='image/increase_business.png'))


@app.route("/image/search_icon.svg")
def search_icon_svg():
    return redirect(url_for("static", filename='image/search_icon.svg'))


@app.route("/image/gold.png")
def gold_png():
    return redirect(url_for("static", filename='image/gold.png'))


@app.route("/image/bucket_paint.png")
def bucket_paint_png():
    return redirect(url_for("static", filename='image/bucket_paint.png'))

