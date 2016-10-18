# phonenumberinfo

### Introduction
An api accepting a phone number as input and providing information on that number.

### Set up environment
* install pip for managing python and its packages
* Setup a virtual environment for your python using instructions at http://virtualenvwrapper.readthedocs.io/en/latest/install.html
* mkvirtualenv phoneinfo
* workon phoneinfo
* pip install -r requirements
* At this point your environment is all set to run tests.

### Usage information
* run ```python manage.py runserver``` inside the phonenumberinfo dir
* you should be able to hit the API at http://localhost:8000
* try 'http://localhost:8000/info/phone_number/6786786780' for querying a single number against the US market
* try 'http://localhost:8000/info/phone_number/6786786780/IN' for querying a single number against country = India
* try 'http://localhost:8000/info/phone_number/100' for querying a single number against the US market and you should see a result of "Valid number = False"
* try 'http://localhost:8000/info/current/time' for getting the current time
* try 'http://localhost:8000/info/current/date' for getting the current date.
