# django-next-starter

Starter project for djangorestframework in the backend and next.js react app in the front

## TODO
1. Add mutations
2. Set up working example with Apollo querying data in the frontend

## Usage
- Create VM with virtualenvwrapper and add the following to the postactivate script:
```
export DJANGO_SETTINGS_MODULE=backend.settings.dev
```
- Create `.env` file with SECRET_KEY, DEBUG, ALLOWED_HOSTS & DATABASE_URL
- Clone, create db, run migrations, create user
```
git clone git@github.com:jcaguirre89/django-next-starter.git
python manage.py create_db
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

