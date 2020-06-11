# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Adn(db.Model):
    __tablename__ = 'adn'

    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.ForeignKey('type.id'), nullable=False, index=True)
    adn = db.Column(db.String(200), nullable=False)
    create_at = db.Column(db.DateTime, server_default=db.FetchedValue())

    type = db.relationship('Type', primaryjoin='Adn.type_id == Type.id', backref='adns')



class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    create_at = db.Column(db.DateTime, server_default=db.FetchedValue())



class Type(db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
