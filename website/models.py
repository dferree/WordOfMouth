from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Boolean

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.Relationship('Note')
    activities = db.Relationship('Activity')
    reviews = db.Relationship('Review')
    
class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(500))
    activity = db.Column(Boolean, default=False)
    adult_ent = db.Column(Boolean, default=False)
    bakery = db.Column(Boolean, default=False)
    comedy_club = db.Column(Boolean, default=False)
    music_venue = db.Column(Boolean, default=False)
    nightclub = db.Column(Boolean, default=False)
    nightlife = db.Column(Boolean, default=False)
    outdoors = db.Column(Boolean, default=False)
    restaurant = db.Column(Boolean, default=False)
    visited = db.Column(Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reviews = db.Relationship('Review', backref='activity_reviews', lazy='dynamic')
    
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500))
    rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'))
    activity = db.Relationship('Activity')


    
