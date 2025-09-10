from flask_sqlalchemy import SQLAlchemy

# Global SQLAlchemy instance for use across the application
# It will be initialised with the Flask app in app.py

db = SQLAlchemy()


class Database(db.Model):
    """Stores information about a database instance."""

    __tablename__ = "databases"

    # The database name acts as the primary key so that other tables
    # can reference it directly.
    name = db.Column(db.String(128), primary_key=True)
    environment = db.Column(db.String(64))
    db_type = db.Column(db.String(64))
    version = db.Column(db.String(64))
    dblink_name = db.Column(db.String(128))
    description = db.Column(db.Text)


class Account(db.Model):
    """Represents an account within a database."""

    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    account_type = db.Column(db.String(64))
    description = db.Column(db.Text)

    # Foreign key constraint referencing Database.name
    database_name = db.Column(
        db.String(128), db.ForeignKey("databases.name"), nullable=False
    )

    # Establish relationship back to the Database model
    database = db.relationship(
        "Database", backref=db.backref("accounts", cascade="all, delete-orphan", lazy=True)
    )
