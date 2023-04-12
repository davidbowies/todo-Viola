from flask import Blueprint, render_template, request, current_app, redirect, url_for, jsonify
from app.tasks_aka_cookies.models import Task, Category
from app.extensions.database import db
from datetime import datetime
# from app.todo_aka_orders.models import Tag, TaskTag, Note
# from app.todo_aka_orders.action.create_task import create_task


blueprint = Blueprint('tasks_aka_cookies', __name__)

@blueprint.route("/general")
def general():
     new_task = Task.query.all()
     return render_template('general.html', tasks=new_task)


@blueprint.before_app_first_request
def create_tables():
    db.create_all()

# @blueprint.route('/')
# def index():
#     return redirect(url_for('tasks'))

# @blueprint.route('/tasks')
# def tasks():
#     tasks = Task.query.all()
#     return render_template('tasks.html', tasks=tasks)

@blueprint.route('/tasks/new', methods=['GET', 'POST'])
def new_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        whendue = datetime.strptime(request.form['whendue'], '%Y-%m-%d') if request.form['whendue'] else None
        completed = request.form.get('completed') == 'on'
        categories = request.form.getlist('categories')
        task = Task(title=title, description=description, whendue=whendue, completed=completed)
        for category_id in categories:
            category = Category.query.get(category_id)
            task.category.append(category)
        db.session.add(task)
        db.session.commit()
        return render_template('tasks_aka_cookies/new_task.html', categories=categories)
    categories = Category.query.all()
    # redirecvt to tastk/id/edit
    return render_template('tasks_aka_cookies/new_task.html', categories=categories)

@blueprint.route('/task/<int:id>/edit', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get(id)
    categories = Category.query.all()
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.whendue = datetime.strptime(request.form['whendue'], '%Y-%m-%d') if request.form['whendue'] else None
        task.completed = bool(request.form.get('completed'))
        task.category = []
        categories = request.form.getlist('categories')
        for category_id in categories:
            category = Category.query.get(category_id)
            task.category.append(category)
        db.session.commit()
        # return redirect(url_for('tasks_aka_cookies.new_task'))
    return render_template('edit_task.html', task=task, categories=categories)

@blueprint.route('/tasks/<int:id>/delete', methods=['DELETE', 'POST'])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    if request.method == 'DELETE':
        return redirect(url_for('tasks_aka_cookies.general'))
    else:
        return render_template('delete_task.html', task=task)



@blueprint.route('/tasks/list')
def get_list():
    tasks = Task.query.all()
    return render_template('task_detail.html', tasks=tasks)








# @blueprint.route('/tasks/<slug>')
# def task(slug):
#      task = Task.query.filter_by(slug=slug).first_or_404()
#      return render_template('tasks/show.html', task=task)

# @blueprint.route('/tasks')
# def tasks():
#      page_number = request.args.get('page', 1, type=int)
#      tasks_pagination = Task.query.paginate(page_number, current_app.config['COOKIES_PER_PAGE'])
#      return render_template('tasks/index.html', tasks_pagination=tasks_pagination)









# @blueprint.route('/tasks')
# def task_list():
#      page = request.args.get('page', 1, type=int)
#      per_page = request.args.get('per_page', 10, type=int)
#      tasks = Task.query.paginate(page=page, per_page=per_page)
#      return render_template('todo/task_list.html', tasks=tasks, url=request.url)


# @blueprint.route('/task/<int:task_id>')
# def task_detail(task_id):
#       task = Task.query.get(task_id)
#       return render_template('task_detail.html', task=task)




