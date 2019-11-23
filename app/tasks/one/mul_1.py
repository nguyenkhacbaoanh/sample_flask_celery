from app import celery
@celery.task()
def mul(x,y):
    return x*y