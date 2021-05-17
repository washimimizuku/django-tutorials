# udemy-recipe-api

Udemy recipe api tutorial

## Build docker Image

```
$ docker-compose build
```

## Create Django project

```
$ docker-compose run app sh -c "django-admin.py startproject app ."
```

## Test

```
$ docker-compose run app sh -c "python manage.py test && flake8"
```

## Run

```
$ docker-compose run app sh -c "python manage.py runserver"
```

## Run migrations

```
$ docker-compose run app sh -c "python manage.py migrate"
```
