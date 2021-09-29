from flask import *
from app.main import app
from app.models import db, article as Article, sign_up as Sign_Up, login as Login


@app.route("/delete/<name>")
def delete(name):
    row = Article.query.filter_by(name=name)

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
            return False

        if password == '':
            return False

        new_user = Sign_Up(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        app.config["username"] = username
        app.config["password"] = password

        return render_template("setCookie.html", username=username, password=password)
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

        try:
            table = Sign_Up.query.filter_by(username=username).first()

            if password == table.password:
                user = Login(username=username, password=password)
                db.session.add(user)
                db.session.commit()

                app.config['username'] = username
                app.config['password'] = password

                return render_template("setCookie.html", username=username, password=password)
            else:
                return render_template("alert_error.html", alert='There was a problem with your login.')
        except:
            return render_template("alert_error.html", alert='There was a problem with your login.')

    return render_template("login.html")


@app.route("/article/<name>")
def article(name):
    table = Article.query.filter_by(name=name)
    return render_template("article.html", name=name, table=table)


@app.route("/news")
def news():
    return render_template("news.html")


@app.errorhandler(404)
def halaman_tidak_ditemukan(e):
    return redirect(url_for("Home"))


@app.route("/")
def Home():
    # Table
    try:
        username = app.config["username"]

        tables = Article.query.filter_by(user=username)

        return render_template("home.html", tables=tables, username=username)
    except KeyError:
        return redirect(url_for("login"))


@app.route("/edit/<name>", methods=['GET', 'POST'])
def edit(name):
    if request.method == 'POST':
        content = request.form['content']
        background = request.form['background']

        table = Article.query.filter_by(name=name).first()

        table.content = content
        table.background = background

        db.session.commit()

        return redirect("/article/%s" % (name))

    table = Article.query.filter_by(name=name).first()

    content = table.content

    return render_template("edit.html", name=name, tables=table, content=content)


@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        content = request.form['content']
        name = request.form['title']
        background = request.form['background']

        exist = db.session.query(db.exists().where(Article.name == name)).scalar()

        if exist == True:
            return render_template("error_already_exist.html", name=name)

        if name == "":
            return False

        if content == "":
            return False

        new_article = Article(name=name, content=content, user=app.config["username"], background=background)
        db.session.add(new_article)
        db.session.commit()
        return redirect("/article/%s" % (name))

    return render_template("new.html")


from app.image import *
