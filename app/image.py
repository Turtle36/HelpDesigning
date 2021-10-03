from app.main import app
from flask import url_for, redirect


@app.route("/image/icon.png")
def icon():
    return redirect(url_for("static", filename='image/icon.png'))


@app.route("/image/error.png")
def error_png():
    return redirect(url_for("static", filename='image/error.png'))


@app.route("/image/up_business.png")
def increase_business_png():
    return redirect(url_for("static", filename='image/up_business.png'))


@app.route("/image/new_article.png")
def new_article_png():
    return redirect(url_for("static", filename='image/new_article.png'))


@app.route("/image/search_icon.png")
def search_icon_svg():
    return redirect(url_for("static", filename='image/search_icon.png'))


@app.route("/image/gold.png")
def gold_png():
    return redirect(url_for("static", filename='image/gold.png'))


@app.route("/image/bucket_paint.png")
def bucket_paint_png():
    return redirect(url_for("static", filename='image/bucket_paint.png'))

