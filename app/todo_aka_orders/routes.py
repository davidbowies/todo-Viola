from flask import Blueprint, render_template, redirect, url_for, request, current_app, abort, flash
from app.extensions.database import db
from app.tasks_aka_cookies.models import Task
from app.todo_aka_orders.models import Tag, TaskTag, Note
from app.todo_aka_orders.action.create_task import create_task

blueprint = Blueprint('todo_aka_orders', __name__)

@blueprint.get('/list')
def get_list():
    tasks = Task.query.all()
    return render_template('action/create_task.html', tasks=tasks)

@blueprint.post('/list')
def post_list():
    try: 
      tasks = Task.query.all()

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
      

# blueprint = Blueprint('todo_aka_orders', __name__, url_prefix='/todo')

# @blueprint.route('/new-task', methods=['GET', 'POST'])
# def new_task():
#     form = TaskForm()

#     if form.validate_on_submit():
#         task = Task(
#             title=form.title.data,
#             description=form.description.data,
#             completed=form.completed.data,
#             category_id=form.category.data.id if form.category.data else None,
#         )
#         db.session.add(task)
#         db.session.commit()
#         return redirect(url_for('todo_aka_orders.task_list'))

#     return render_template('todo/new_task.html', form=form)

# @blueprint.route('/tasks')
# def task_list():
#     page = request.args.get('page', 1, type=int)
#     per_page = request.args.get('per_page', 10, type=int)
#     tasks = Task.query.paginate(page=page, per_page=per_page)
#     return render_template('todo/task_list.html', tasks=tasks, url=request.url)

# @blueprint.route('/task/<int:task_id>')
# def task_detail(task_id):
#     task = Task.query.get(task_id)
#     if not task:
#         abort(404)
#     return render_template('todo/task_detail.html', task=task)

# @blueprint.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
# def edit_task(task_id):
#     task = Task.query.get(task_id)
#     if not task:
#         abort(404)

#     form = TaskForm(obj=task)
#     if form.validate_on_submit():
#         task.title = form.title.data
#         task.description = form.description.data
#         task.completed = form.completed.data
#         task.category_id = form.category.data.id if form.category.data else None
#         db.session.commit()
#         return redirect(url_for('todo_aka_orders.task_detail', task_id=task.id))

#     return render_template('todo/edit_task.html', form=form, task=task)

# @blueprint.route('/task/<int:task_id>/delete', methods=['POST'])
# def delete_task(task_id):
#     task = Task.query.get(task_id)
#     if not task:
#         abort(404)

#     db.session.delete(task)
#     db.session.commit()
#     flash('Task deleted successfully', 'success')
#     return redirect(url_for('todo'))
