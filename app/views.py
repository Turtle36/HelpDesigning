from flask import *
from app.main import app
from app.models import db, article as Article, sign_up as Sign_Up, login as Login, User

User = User()


@app.route("/support")
def support():
    return render_template("support.html")


@app.route("/edit/<name>", methods=['GET', 'POST'])
def edit(name):
    if request.method == 'POST':
        content = request.form['content']

        table = Article.query.filter_by(name=name, user=User.getUsername()).first()

        table.content = content

        db.session.commit()

        return redirect(url_for("Home"))

    table = Article.query.filter_by(name=name).first()

    content = table.content

    return render_template("edit.html", name=name, tables=table, content=content)


@app.route("/image /icon.png")
def icon():
    return redirect(url_for("static", filename='image/icon.png'))


@app.route("/image/earth.gif")
def earth_gif():
    return redirect(url_for("static", filename='image/earth.gif'))


@app.route("/delete/<name>")
def delete(name):
    row = Article.query.filter_by(name=name, user=User.getUsername())

    row.delete()

    db.session.commit()

    return redirect(url_for("Home"))


@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        exist = db.session.query(db.exists().where(Sign_Up.username == username)).scalar()

        if exist == True:
            return render_template("alert_error.html", alert=""""%s" Already Exist""" % username)

        if username == '':
            return redirect(url_for("Home"))

        if password == '':
            return redirect(url_for("Home"))

        new_user = Sign_Up(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        SignUp = User.SignUp()

        SignUp.setUsername(username)
        SignUp.setPassword(password)

        User.setUsername(username)
        User.setPassword(password)

        return redirect(url_for("Home"))

    return render_template("signup.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == '':
            return False

        if password == '':
            return False

        SignUp = User.SignUp()

        table = Sign_Up.query.filter_by(username=SignUp.getUsername())
        LOGIN = User.Login()

        LOGIN.setUsername(username)
        LOGIN.setPassword(password)
        User.setUsername(username)
        User.setPassword(password)

        for tables in table:
            if password == tables.password:
                "Required"

                user = Login(username=username, password=password)
                db.session.add(user)
                db.session.commit()
            else:
                return render_template("alert_error.html", alert='There was a problem with your login.')

    return render_template("login.html")


@app.route("/image/search_icon.png")
def search_icon_png():
    return redirect(url_for("static", filename='image/searchicon.png'))


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

        new_article = Article(name=name, content=content, user=User.getUsername())
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


@app.route("/")
def Home():
    # Table
    table = Article.query.filter_by(user=User.getUsername())

    return render_template("home.html", tables=table)
