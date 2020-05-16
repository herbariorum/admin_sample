from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(255))
    email = db.Column(db.String(100))
    update_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<User {}'.format(self.username)
