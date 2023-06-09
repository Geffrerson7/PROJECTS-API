from app.db import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    phone_number = db.Column(db.String(20))
    password = db.Column(db.String(255))
    date_born = db.Column(db.Date)
    last_session = db.Column(db.DateTime, default=None)
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    created_at = db.Column(db.DateTime, default=func.now())

    def __init__(self, name, email, phone_number, password, date_born):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.password = password
        self.date_born = date_born