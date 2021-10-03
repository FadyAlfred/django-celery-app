Django Celery Sample App
---

### Introduction

This is a sample app with only 2 celery tasks for demonstrating the async tasks in celery 

### Technologies

Django Celery App uses a number of open source projects to work properly:

* [Python](https://www.python.org) - is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible.
* [Pip](https://pypi.org/project/pip/) - is a package-management system written in Python used to install and manage software packages.
* [Django](https://www.djangoproject.com/) - is an open source asynchronous task queue or job queue which is based on distributed message passing. While it supports scheduling, its focus is on operations in real time.
* [Celery](https://docs.celeryproject.org/en/stable/) - is architectural style for distributed hypermedia systems.
* [Flower](https://flower.readthedocs.io/en/latest/) -  is a web based tool for monitoring and administrating Celery clusters
* [Docker](https://www.docker.com/) - is a set of platform as a service (PaaS) products that use OS-level virtualization.

### Install and run

```sh
$ Clone the repository and go into the project
$ Create a virtual env and activate it
$ Install the reqirements using this command `pip install requirements.txt`
$ Migrate using this command `python manage.py migrate`
$ Craete superuser using this command `python manage.py createsuperuser`
$ Run the application using this command `python manage.py runserver`
$ The app should be up and running on localhost:8000
$ The app admin should be up and running on localhost:8000/admin
```

### Run Redis
```sh
$ Install docker on your local machine
$ Run redis using the following command `docker run --name my-redis-server -d -p 127.0.0.1:6379:6379 redis`
```

### Run celery and flower
```sh
$ In new terminal run celery using `celery -A django_celery worker -l info -P solo`
$ In new terminal run flower using `celery -A django_celery flower`
$ Flower app should be up and running on localhost:5555
```

### Testing
```sh
$ Open django shell using this command `python manage.py shell`
$ Import debug task `from django_celery.celery import debug_task`
$ Import create user task `from core.tasks import create_user`
$ Create instance of debug task `debug_task.apply_async(countdown=10)`
$ Check the result in celery terminal and flower
$ Create instance of debug task `create_user.apply_async(countdown=10)`
$ Check the result in celery terminal and flower
$ Login to admin and check if new user created 
```

### Todos
 - Dockerize the application
 - Use docker compose to simplify the project run and deployment