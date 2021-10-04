from flask import *
from app.main import app
from app.models import db, article as Article, sign_up as Sign_Up, login as Login, customers as Customers


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
        new_row = Customers(customer=0, user=username)
        db.session.add(new_user)
        db.session.add(new_row)
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

                app.config["username"] = username
                app.config["password"] = password

                return render_template("setCookie.html", username=username, password=password)
            else:
                return render_template("alert_error.html", alert='Invalid password')
        except:
            return render_template("alert_error.html", alert='User not found')

    return render_template("login.html")


@app.route("/article/<name>")
def article(name):
    table = Article.query.filter_by(name=name)
    for Table in table:
        Table.customer += 1
        tables = Customers.query.filter_by(user=Table.user)
        for MyTables in tables:
            MyTables.customer += 1
    db.session.commit()
    return render_template("article.html", name=name, table=table)


@app.route("/news")
def news():
    try:
        username = app.config["username"]
        return render_template("news.html")
    except:
        return redirect(url_for("login"))


@app.errorhandler(404)
def halaman_tidak_ditemukan(e):
    return redirect(url_for("homepage"))


@app.route("/article")
def all_article():
    try:
        username = app.config["username"]

        # Table
        tables = Article.query.all()

        return render_template("all_article.html", tables=tables, username=username)
    except KeyError:
        return redirect(url_for("login"))


@app.route("/home")
def Home():
    try:
        username = app.config["username"]

        Tables = Customers.query.filter_by(user=username)
        tables = Article.query.filter_by(user=username)
        for table in Tables:
            customer = table.customer

            return render_template("home.html", tables=tables, username=username, customer=customer)
    except KeyError:
        return redirect(url_for("login"))


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/edit/<name>", methods=['GET', 'POST'])
def edit(name):
    if request.method == 'POST':
        content = request.form['content']
        background = request.form['background']

        table = Article.query.filter_by(name=name)
        for tables in table:
            tables.content = content
            tables.background = background

        db.session.commit()

        return redirect("/article/%s" % (name))

    table = Article.query.filter_by(name=name)

    for tables in table:
        content = tables.content

        try:
            username = app.config["username"]
        except:
            return redirect(url_for("Home"))

        return render_template("edit.html", name=name, tables=table, content=content)


@app.route("/new/article", methods=['GET', 'POST'])
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

    try:
        username = app.config["username"]

        return render_template("new.html")
    except:
        return redirect(url_for("login"))


from app.image import *
