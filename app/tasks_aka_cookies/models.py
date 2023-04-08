#from flask import Flask, render_template, request, redirect, url_for
from app.extensions.database import db, CRUDMixin
#from flask_sqlalchemy import SQLAlchemy

class Task(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=True)
    whendue = db.Column(db.DateTime)
    completed = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('tasks', lazy=True))

class Category(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(80), nullable=False)

task_categorie = db.relationship('TaskCategorie', backref='tasks', lazy=True)