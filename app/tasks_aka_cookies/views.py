# from flask import Blueprint, render_template, request, redirect, url_for, flash
# from app.extensions.database import db
# from app.tasks_aka_cookies.models import Task, Category, TaskCategory


# blueprint = Blueprint('tasks_aka_cookies', __name__)


# @blueprint.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         title = request.form['title']
#         description = request.form['description']
#         whendue = request.form['whendue']
#         completed = False
#         category_id = request.form['category_id']

#         task = Task(title=title, description=description, whendue=whendue,
#                     completed=completed, category_id=category_id)

#         db.session.add(task)
#         db.session.commit()

#         flash('Task created successfully!', 'success')

#         return redirect(url_for('tasks_aka_cookies.index'))

#     tasks = Task.query.all()

#     return render_template('index.html', tasks=tasks)


# @blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit(id):
#     task = Task.query.get_or_404(id)

#     if request.method == 'POST':
#         task.title = request.form['title']
#         task.description = request.form['description']
#         task.whendue = request.form['whendue']
#         task.completed = request.form.get('completed') == 'on'
#         task.category_id = request.form['category_id']

#         db.session.commit()

#         flash('Task updated successfully!', 'success')

#         return redirect(url_for('tasks_aka_cookies.index'))

#     categories = Category.query.all()

#     return render_template('edit.html', task=task, categories=categories)


# @blueprint.route('/delete/<int:id>', methods=['GET', 'POST'])
# def delete(id):
#     task = Task.query.get_or_404(id)

#     if request.method == 'POST':
#         db.session.delete(task)
#         db.session.commit()

#         flash('Task deleted successfully!', 'success')

#         return redirect(url_for('tasks_aka_cookies.index'))

#     return render_template('delete.html', task=task)