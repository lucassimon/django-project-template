django-project-template
=======================

Django 1.6+ Base Template
-------------------------

How to use this template to create your project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Create your virtualenv
- Install Django 
- $ django-admin.py startproject --template https://github.com/ryanrdetzel/django-base-template/zipball/master --extension py,md projectname
- $ cd projectname
- $ pip install -r requirements/dev.txt
- $ ./manage.py syncdb --settings=projectname.settings.dev
- $ ./manage.py runserver --settings=projectname.settings.dev

Adding an app
~~~~~~~~~~~~~

- $ python manage.py startapp --template https://github.com/lucassimon/django-app-template/zipball/master app_name
- add app_name to INSTALLED_APPS projectname/settings/base.py

## About ##

## Prerequisites ##

- Python >= 2.5
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)


