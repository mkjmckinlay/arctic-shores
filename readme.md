# Arctic Shores - Technical Task

## Requirements

The task has been completed using Python 3.8 and Django 2.2.9.

##Overview

Django has been used to create a candidate class and a Score Class.

The import and sort scripts have been written in pure Python.

##Assumptions

- Pyhon 3.8 is installed on the machine and available from the CLI as python38
- Virtualenvwrapper is installed

##Instructions


1. create a folder and clone the repo into it
    ```python
    mkdir arctic-shores
    cd arctic-shores
    git clone git@github.com:mkjmckinlay/arctic-shores.git . 
    ```
 
2. Create a Virtual Enviroment and then activate it
    ```python
    mkvirtualenv -p /usr/bin/python38 venv
   . venv/bin/activate
    ```
 3. install the requirements
    ```python
    pip install requirements.txt
    ```
 
 4. create the database and admin user
    ```python
    python manage.py migrate
    python manage.py createsuperuser
    ```
    
 5. Start the Django Webserver
    ```python
    python manage.py runserver 0.0.0.0:8000
    ```
    
 6. 