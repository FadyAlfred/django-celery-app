import string
import random

from django_celery.celery import app


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.task(bind=True)
def create_user(self):
    from django.contrib.auth.models import User
    username = id_generator()
    user = User.objects.create_user(username=username, password='glass onion')
    return user.username
