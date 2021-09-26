from app.main import *


@app.route("/image/icon.png")
def icon():
    return redirect(url_for("static", filename='image/icon.png'))


@app.route("/image/earth.gif")
def earth_gif():
    return redirect(url_for("static", filename='image/earth.gif'))
