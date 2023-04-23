from flask import Blueprint, render_template
from app.tasks_aka_cookies.models import Task

blueprint = Blueprint('simple_pages', __name__)


@blueprint.route('/')
def index():
    tasks = Task.query.all()
    return render_template('tasks/index.html', tasks=tasks)


@blueprint.route('/studies')
def studies():
     return render_template('studies.html')


@blueprint.route("/private")
def private():
    tasks = Task.query.all()
    return render_template('private.html', tasks=tasks)


@blueprint.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)


