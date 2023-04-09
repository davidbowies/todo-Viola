from app.app import create_app
from app.extensions.database import db
from app.tasks_aka_cookies.models import Task
from datetime import datetime

if __name__ == '__main__':
  app = create_app()
  app.app_context().push()

  to_do_list = {
     '1' : {'description': 'Complete project proposal', 'completed': 'in progress'},
     '2' : {'description': 'Attend meeting with team', 'completed': 'complete'},
     '3' : {'description': 'Research competitors', 'completed': 'not started'},
     '4' : {'description': 'Create wireframe designs', 'completed': 'in progress'},
     '5' : {'description': 'Review feedback from stakeholders', 'completed': 'not started'},
     '6' : {'description': 'Finalize project plan', 'completed': 'complete'}
  }

  for title, task in to_do_list.items():
    new_task = Task(title=title, description=task['description'], completed=task['completed'])
    db.session.add(new_task)

  db.session.commit()
