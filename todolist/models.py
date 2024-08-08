from datetime import datetime
from todolist import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nick_name = db.Column(db.String(10), nullable=False, unique=True)


class Week(db.Model):
    __tablename__ = 'weeks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monday = db.Column(db.DateTime, default=datetime.utcnow)
    tuesday = db.Column(db.DateTime, default=datetime.utcnow)
    wednesday = db.Column(db.DateTime, default=datetime.utcnow)
    thursday = db.Column(db.DateTime, default=datetime.utcnow)
    friday = db.Column(db.DateTime, default=datetime.utcnow)
    saturday = db.Column(db.DateTime, default=datetime.utcnow)
    sunday = db.Column(db.DateTime, default=datetime.utcnow)
    owner = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=True)
    status = db.Column(db.Boolean, default=False, nullable=False)
    belong = db.Column(db.Integer, db.ForeignKey('weeks.id'), nullable=False)
