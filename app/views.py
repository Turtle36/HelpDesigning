from flask import *
from app.main import app
from app.models import db, Article


@app.route("/support")
def support():
    return render_template("support.html")


@app.route("/edit/<name>", methods=['GET', 'POST'])
def edit(name):
    if request.method == 'POST':
        content = request.form['content']

        table = Article.query.filter_by(name=name).first()

        table.content = content

        db.session.commit()

        return redirect(url_for("Home"))

    table = Article.query.filter_by(name=name).first()

    content = table.content

    return render_template("edit.html", name=name, tables=table, content=content)


@app.route("/", methods=['GET', 'POST'])
def Home():
    # Table
    table = Article.query.all()

    if request.method == 'POST':
        search = request.form['search']

        table = Article.query.filter(Article.name.like('%' + search + '%')).all()

    return render_template("home.html", tables=table)


@app.route("/image/icon.png")
def icon():
    return redirect(url_for("static", filename='image/icon.png'))


@app.route("/image/earth.gif")
def earth_gif():
    return redirect(url_for("static", filename='image/earth.gif'))


@app.route("/delete/<name>")
def delete(name):
    row = Article.query.filter_by(name=name)

    row.delete()

    db.session.commit()

    return redirect(url_for("Home"))


@app.route("/article/<name>")
def article(name):
    table = Article.query.filter_by(name=name)
    return render_template("article.html", name=name, table=table)


@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        content = request.form['content']

        name = request.form['title']

        exist = db.session.query(db.exists().where(Article.name == name)).scalar()

        if exist == True:
            return render_template("error_already_exist.html", name=name)

        if name == "":
            return False

        if content == "":
            return False

        new_article = Article(name=name, content=content)
        db.session.add(new_article)
        db.session.commit()
        return redirect("/article/%s" % name)

    return render_template("new.html")


@app.route("/image/error.png")
def error_png():
    return redirect(url_for("static", filename='image/error.png'))


@app.errorhandler(404)
def halaman_tidak_ditemukan(e):
    return redirect(url_for("Home"))
