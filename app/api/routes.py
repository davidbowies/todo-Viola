from flask import Blueprint, jsonify
from app.tasks_aka_cookies.models import Task
from os import environ

blueprint = Blueprint('api', __name__)


@blueprint.get('/api/v1/todo_aka_orders')
def todo():
    if environ.get('API_KEY') == request.args.get('key'):
        tasks = Task.query.all()
        return jsonify({
         "data": "Hello World"
        })
    else:
        return jsonify({'error': 'Invalid API key'}), 401
     