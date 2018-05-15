from flaskblog import celery


@celery.task()
def add_together(a, b):
    result = a + b
    print(result)
    return result
