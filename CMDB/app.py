from datetime import datetime

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

    @app.context_processor
    def inject_current_date():
        """Provide current date for templates."""
        return {"current_date": datetime.now().strftime("%B %d, %Y")}

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


    @app.route("/database/<string:name>/edit", methods=["GET", "POST"])
    def edit_database(name):
        """Edit metadata for an existing database."""
        database = Database.query.get_or_404(name)
        if request.method == "POST":
            database.environment = request.form.get("environment")
            database.db_type = request.form.get("db_type")
            database.version = request.form.get("version")
            database.description = request.form.get("description")
            db.session.commit()
            return redirect(url_for("database_detail", name=name))
        return render_template("edit_database.html", database=database)

    @app.route("/database/<string:name>/delete", methods=["POST"])
    def delete_database(name):
        """Remove a database and all associated accounts."""
        database = Database.query.get_or_404(name)
        db.session.delete(database)
        db.session.commit()
        return redirect(url_for("index"))

    @app.route(
        "/database/<string:database_name>/accounts/<int:account_id>/edit",
        methods=["GET", "POST"],
    )
    def edit_account(database_name, account_id):
        """Edit an existing account entry."""
        database = Database.query.get_or_404(database_name)
        account = Account.query.filter_by(id=account_id, database=database).first_or_404()
        if request.method == "POST":
            account.username = request.form["username"]
            account.password = request.form["password"]
            account.account_type = request.form.get("account_type")
            account.dblink_name = request.form.get("dblink_name")
            account.description = request.form.get("description")
            db.session.commit()
            return redirect(url_for("database_detail", name=database_name))
        return render_template("edit_account.html", database=database, account=account)

    @app.route(
        "/database/<string:database_name>/accounts/<int:account_id>/delete",
        methods=["POST"],
    )
    def delete_account(database_name, account_id):
        """Delete an account from a database."""
        account = Account.query.filter_by(
            id=account_id, database_name=database_name
        ).first_or_404()
        db.session.delete(account)
        db.session.commit()
        return redirect(url_for("database_detail", name=database_name))


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
