from app import celery
import time
@celery.task()
def add(x,y):
    return x + y