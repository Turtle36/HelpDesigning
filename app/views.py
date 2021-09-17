from flask import *
from app.main import app
from app.models import db, Table


@app.route("/premium")
def premium():
    return render_template("premium.html")


@app.route("/support")
def support():
    return render_template("support.html")


@app.route("/edit/<name>", methods=['GET', 'POST'])
def edit(name):
    if request.method == 'POST':
        content = request.form['content']
        title = request.form['Name']

        table = Table.query.filter_by(name=name).first()

        exist = db.session.query(db.exists().where(Table.name == name)).scalar()

        if exist == True:
            return render_template("error_already_exist.html", name=name)

        table.content = content
        table.name = title

        db.session.commit()

        return redirect(url_for("Home"))

    table = Table.query.filter_by(name=name).first()

    page_name = table.name

    content = table.content

    return render_template("edit.html", name=name, tables=table, page_name=page_name, content=content)


@app.route("/", methods=['GET', 'POST'])
def Home():
    # Table
    table = Table.query.all()

    if request.method == 'POST':
        search = request.form['search']

        table = Table.query.filter(Table.name.like('%' + search + '%')).all()

    return render_template("home.html", tables=table)


@app.route("/image/icon.png")
def icon():
    return redirect(url_for("static", filename='image/icon.png'))


@app.route("/image/earth.gif")
def earth_gif():
    return redirect(url_for("static", filename='image/earth.gif'))

@app.route("/delete/<name>")
def delete(name):
    row = Table.query.filter_by(name=name)

    row.delete()

    db.session.commit()

    return redirect(url_for("Home"))


@app.route("/article/<name>")
def page(name):
    table = Table.query.filter_by(name=name).all()
    return render_template("page.html", name=name, table=table)


@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        content = request.form['content']

        name = request.form['Name']

        exist = db.session.query(db.exists().where(Table.name == name)).scalar()

        if exist == True:
            return render_template("error_already_exist.html", name=name)
        else:
            "None"

        if name == "":
            return False

        if content == "":
            return False

        new_page = Table(name=name, content=content)
        db.session.add(new_page)
        db.session.commit()
        return redirect("/article/%s" % name)

    return render_template("new.html")


@app.route("/image/error.png")
def error_png():
    return redirect(url_for("static", filename='image/error.png'))


@app.errorhandler(404)
def halaman_tidak_ditemukan(e):
    return redirect(url_for("Home"))
