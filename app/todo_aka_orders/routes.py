from flask import Blueprint, render_template, redirect, url_for, request, current_app, abort, flash
from app.extensions.database import db
from app.tasks_aka_cookies.models import Task
from app.todo_aka_orders.models import Tag, TaskTag, Note
from app.todo_aka_orders.action.create_task import create_task

blueprint = Blueprint('todo_aka_orders', __name__)

@blueprint.get('/list')
def get_list():
    tasks = Task.query.all()
    return render_template('action/task_list.html', tasks=tasks)


@blueprint.post('/list')
def post_list():
    tasks = Task.query.all()
    try: 
        if not all([
           request.form.get('body'),
           request.form.get('created_at')
        ]):
            raise Exception('Please fill out, when created.')
        
        create_task(request.form, tasks)
        return render_template('action/create_task.html', tasks=tasks)
    except Exception as error_message:
        error = error_message or 'An error occured when dtrying to fill out the form, plase enter valid data.'

        current_app.logger.info(f'Error filling out the form: {error}')

        return render_template('action/create_task.html',
            tasks=tasks,
            error=error
        )


@blueprint.route('/task/<int:task_id>')
def task_detail(task_id):
     task = Task.query.get(task_id)
     if not task:
         abort(404)
     return render_template('/task_detail.html', task=task)
