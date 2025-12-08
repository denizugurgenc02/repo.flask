from flaskr.extensions import db


class Table(db.Model):
    __tablename__ = "tables"

    id = db.Column(db.Integer, primary_key=True)
