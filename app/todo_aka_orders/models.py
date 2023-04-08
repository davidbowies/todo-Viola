from app.extensions.database import db, CRUDMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class Tag(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False, unique=True)

class TaskTag(db.Model, CRUDMixin):
  task_id = db.Column(db.Integer, db.ForeignKey('task.id'), primary_key=True)
  tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
  task = db.relationship('Task', backref='tags', lazy=True)
  tag = db.relationship('Tag', backref='tasks', lazy=True)

  __table_args__ = (
    db.UniqueConstraint('task_id', 'tag_id'),
  )


class Note(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(500))
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
  task = db.relationship('Task', backref='notes', lazy=True)


