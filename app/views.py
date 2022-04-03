from flask import *
from app.main import app
from app.models import db, article as Article, sign_up as Sign_Up, login as Login, customers as Customers, comment as Comment


@app.route("/delete/article/<name>", methods=['GET', 'POST'])
def delete(name):
    if request.method == "POST":
        row = Article.query.filter_by(name=name)
        for rows in row:
            Customer = Customers.query.filter_by(username=rows.user)
            for customers in Customer:
                customers.customer -= rows.customer
                Article.query.filter_by(name=name).delete()
                db.session.commit()

                return redirect(url_for("home"))

    table = Article.query.filter_by(name=name)

    for tables in table:
        creator = tables.user

        return render_template("delete_article.html", creator=creator)


@app.route("/home")
def home():
    customersTable = Customers.query.all()
    article = Article.query.all()

    return render_template("home.html", customers=customersTable, article=article)


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

                return render_template("setCookie.html", username=username, password=password)
            else:
                return render_template("error.html", alert='Invalid password', route="login")
        except:
            return render_template("error.html", alert='User not found', route="login")

    return render_template("login.html")


@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        exist = db.session.query(db.exists().where(Sign_Up.username == username)).scalar()

        if username == 'Anonymous':
            return render_template("error.html", alert="Username Cannot \"Anonymous\"", route="sign_up")

        if exist == True:
            return render_template("error.html", alert=""""%s" Already Exist""" % username)

        if username == '':
            return False

        if password == '':
            return False

        new_user = Sign_Up(username=username, password=password)
        new_row_in_table_customer = Customers(customer=0, username=username)
        db.session.add(new_user)
        db.session.add(new_row_in_table_customer)
        db.session.commit()

        return render_template("setCookie.html", username=username, password=password)
    return render_template("sign_up.html")


@app.route("/")
def homepage():
    return redirect(url_for("home"))


@app.route("/article")
def all_article():
    article = Article.query.all()
    return render_template("all_article.html", article=article)


@app.route("/article/<name>", methods=['GET', 'POST'])
def article(name):
    if request.method == 'POST':
        comment = request.form['comment']
        user = request.form['user']

        new_comment = Comment(user, comment, name)
        db.session.add(new_comment)
        db.session.commit()

        return redirect("/article/%s" % name)

    table = Article.query.filter_by(name=name)
    tComment = Comment.query.filter_by(articleName=name)
    for Table in table:
        Table.customer += 1
        Customer = Customers.query.filter_by(username=Table.user)
        for customer in Customer:
            customer.customer += 1

    db.session.commit()
    return render_template("article.html", name=name, table=table, TComment=tComment)


@app.route("/edit/article/<name>", methods=['GET', 'POST'])
def edit_article(name):
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
        title = tables.name
        background = tables.background
        creator = tables.user

        return render_template("edit_article.html", creator=creator, name=name, title=title, tables=table, content=content,
                               background=background)


@app.route("/new/article", methods=['GET', 'POST'])
def new_article():
    if request.method == 'POST':
        content = request.form['content']
        name = request.form['title']
        background = request.form['background']
        creator = request.form['creator']

        exist = db.session.query(db.exists().where(Article.name == name)).scalar()

        if exist == True:
            return render_template("error.html", alert="Name \"%s\" Already Exist" % name, route="new/article")

        if name == "":
            return False

        if content == "":
            return False

        if "/" in name:
            return render_template("error.html", route="new/article",
                                   alert="You cannot enter a '?' or '/' in title")

        if "?" in name:
            return render_template("error.html", route="new/article",
                                   alert="You cannot enter a '?' or '/' in title")

        new_article = Article(name=name, content=content, background=background, user=creator)
        db.session.add(new_article)
        db.session.commit()
        return redirect("/article/%s" % (name))

    return render_template("new_article.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


from app.image import *

