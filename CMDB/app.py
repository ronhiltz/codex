from flask import Flask, render_template, request, redirect, url_for
from models import db, Database, Account


def create_app():
    """Application factory for the CMDB UI."""
    app = Flask(__name__)

    # Configure the SQLite database.  In a real deployment this could be
    # pointed at another RDBMS.
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cmdb.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialise the database with this app context.
    db.init_app(app)
    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        """List all databases."""
        databases = Database.query.all()
        return render_template("index.html", databases=databases)

    @app.route("/database/new", methods=["GET", "POST"])
    def new_database():
        """Create a new database entry."""
        if request.method == "POST":
            data = Database(
                name=request.form["name"],
                environment=request.form.get("environment"),
                db_type=request.form.get("db_type"),
                version=request.form.get("version"),
                description=request.form.get("description"),
            )
            db.session.add(data)
            db.session.commit()
            return redirect(url_for("index"))
        return render_template("new_database.html")

    @app.route("/database/<string:name>", methods=["GET", "POST"])
    def database_detail(name):
        """View details for a database and manage its accounts."""
        database = Database.query.get_or_404(name)
        if request.method == "POST":
            account = Account(
                username=request.form["username"],
                password=request.form["password"],
                account_type=request.form.get("account_type"),
                dblink_name=request.form.get("dblink_name"),
                description=request.form.get("description"),
                database=database,
            )
            db.session.add(account)
            db.session.commit()
            return redirect(url_for("database_detail", name=name))
        return render_template("database_detail.html", database=database)


    @app.route("/accounts")
    def accounts():
        """List distinct account usernames."""
        usernames = [row[0] for row in db.session.query(Account.username).distinct().all()]
        return render_template("accounts.html", usernames=usernames)

    @app.route("/accounts/<string:username>")
    def account_detail(username):
        """Show databases where the specified account exists."""
        accounts = Account.query.filter_by(username=username).all()
        return render_template("account_detail.html", username=username, accounts=accounts)

    return app


if __name__ == "__main__":
    app = create_app()
    # Running with debug=True for development convenience.  Remove or set
    # to False in production.
    app.run(debug=True)
