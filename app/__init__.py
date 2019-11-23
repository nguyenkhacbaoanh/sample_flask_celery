import os
from flask import Flask
from celery import Celery

#from app.apis import blueprint

#blueprint = Blueprint('api', __name__)

celery = Celery(__name__, broker="redis://localhost:6379/0", backend="redis://localhost:6379/0", include=["app.tasks.one.add_1", "app.tasks.one.mul_1", "app.tasks.two.add_2", "app.tasks.two.mul_2"])


def create_app():
    app = Flask(__name__)
    #app.register_blueprint(api, url_prefix="/demo")
    #app.config.from_object(config_by_name[config_name])
    celery.conf.update(app.config)
    celery.conf.update(result_expires=3600)
    celery.conf.task_routes = {
        'app.tasks.one.*': {'queue': 'w1'},
        'app.tasks.two.*': {'queue': 'w2'}
    }
    return app

app = create_app()
