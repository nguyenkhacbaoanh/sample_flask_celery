from app import celery
@celery.task(bind=True)
def add(x,y):
    return x + y