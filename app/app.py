from flask import Flask, current_app
from . import tasks_aka_cookies, simple_pages, todo_aka_orders, api
from app.extensions.database import db, migrate

# define your app creation function
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
  #  current_app.config['POSTS_PER_PAGE']

    register_extensions(app)
    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask):
    app.register_blueprint(tasks_aka_cookies.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(todo_aka_orders.routes.blueprint)
    app.register_blueprint(api.routes.blueprint)

# Externsions
def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)



