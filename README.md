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

### Features
* Take a US number by default and provide info on its carrier, if it is a valid number, if it is a possible number and other number based data
* Accept country code as an additional input and provide the  same information for international numbers
* Provide a couple of end points that offer current date and current time

### Usage information
* run ```python manage.py runserver``` inside the phonenumberinfo dir
* you should be able to hit the API at http://localhost:8000/info and see ```{"message": "Hello, you've reached the index. No info here!"}```
* try 'http://localhost:8000/info/phone_number/6786786780' for querying a single number against the US market. This produces ```{"is_number_possible": true, "is_number_valid": true, "number": "6786786780", "national_number": 6786786780, "country_code": 1, "carrier_data": ""}```
* try 'http://localhost:8000/info/phone_number/6786786780/IN' for querying a single number against country = India. This produces ```{"is_number_possible": true, "is_number_valid": true, "number": "9884287789", "national_number": 9884287789, "country_code": 91, "carrier_data": "Vodafone"}```
* try 'http://localhost:8000/info/phone_number/100' for querying a single number against the US market and you should see a result of "Valid number = False". Here's the json response ```{"is_number_possible": false, "is_number_valid": false, "number": "100", "national_number": 100, "country_code": 1, "carrier_data": ""}```
* try 'http://localhost:8000/info/current/time' for getting the current time (```{"time": "13:31:14"}```)
* try 'http://localhost:8000/info/current/date' for getting the current date (```{"date": "18:10:2016"}```)
