# django_url_shortener
A self-learning project that use django to build url shortener and style with Boostrap

# Demo server
[https://url-shortener-django.herokuapp.com/](https://url-shortener-django.herokuapp.com/)

![alt text](http://i.imgur.com/8igbmom.png "preview")


# Installation

## Setting up a development environment
    $ git clone https://github.com/jefftham/django_url_shortener
    $ cd django_url_shortener/
    $ pip install -r requirements.txt
    $ python manage.py makemigrations
    $ python manage.py migrate

## Optional: admin interface
    $ python manage.py createsuperuser

## Run the server
    $ python manage.py runserver

## Optional: change to debug mode
    open: urlShortener/settings.py
    edit: DEBUG = True