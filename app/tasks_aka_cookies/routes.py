from flask import Blueprint, render_template, request, current_app
from app.tasks_aka_cookies.models import Task
# from app.todo_aka_orders.models import Tag, TaskTag, Note
# from app.todo_aka_orders.action.create_task import create_task


blueprint = Blueprint('tasks_aka_cookies', __name__)

@blueprint.route("/general")
def general():
     new_task = Task.query.all()
     return render_template('general.html', tasks=new_task)

@blueprint.route('/tasks/<slug>')
def task(slug):
     task = Task.query.filter_by(slug=slug).first_or_404()
     return render_template('tasks/show.html', task=task)

@blueprint.route('/tasks')
def tasks():
     page_number = request.args.get('page', 1, type=int)
     tasks_pagination = Task.query.paginate(page_number, current_app.config['COOKIES_PER_PAGE'])
     return render_template('tasks/index.html', tasks_pagination=tasks_pagination)

# @blueprint.route('/tasks')
# def task_list():
#      page = request.args.get('page', 1, type=int)
#      per_page = request.args.get('per_page', 10, type=int)
#      tasks = Task.query.paginate(page=page, per_page=per_page)
#      return render_template('todo/task_list.html', tasks=tasks, url=request.url)


# @blueprint.route('/task/<int:task_id>')
# def task_detail(task_id):
#      task = Task.query.get(task_id)
#      return render_template('task_detail.html', task=task)




