from flask import Blueprint, render_template

blueprint = Blueprint('simple_pages', __name__)


@blueprint.route('/')
def index():
    return render_template('tasks/index.html')


@blueprint.route('/studies')
def studies():
     return render_template('studies.html')


@blueprint.route('/private')
def private():
    return render_template('private.html')


@blueprint.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)


