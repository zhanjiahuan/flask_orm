import datetime

from apps.ext import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64),unique=True,index=True,nullable=False)
    price = db.Column(db.Numeric(10, 2),default=0.00)
    status = db.Column(db.Boolean,default=False)
    img = db.Column(db.String(100))
    skill = db.Column(db.String(100))
    create_date = db.Column(db.DateTime,default=datetime.datetime.now())
    desc = db.Column(db.TEXT)
