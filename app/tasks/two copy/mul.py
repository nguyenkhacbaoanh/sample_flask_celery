from app import celery
@celery.task(bind=True)
def mul(x,y):
    return x*y