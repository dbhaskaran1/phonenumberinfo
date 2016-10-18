from django.test import TestCase
from django.test import Client

from models import PhoneInfo

class NumberTestCase(TestCase):
    def setUp(self):
        PhoneInfo.objects.create(phone_number='6786786789', country='US', carrier='AT&T')

    def test_phonenumberprops(self):
        num = PhoneInfo.objects.get(phone_number='6786786789')
        assert num.phone_number == '6786786789'
        assert num.country == 'US'
        assert num.carrier == 'AT&T'

    def test_index_endpoint(self):
        c = Client()
        response = c.get('/info/')
        assert response.status_code == 200

    def test_date_endpoint(self):
        c = Client()
        response = c.get('/info/current/date')
        assert response.status_code == 200

    def test_time_endpoint(self):
        c = Client()
        response = c.get('/info/current/time')
        assert response.status_code == 200

    def test_number_endpoint(self):
        c = Client()
        response = c.get('/info/phone_number/6786786789')
        assert response.status_code == 200

    def test_countrycode_endpoint(self):
        c = Client()
        response = c.get('/info/phone_number/9884287789/IN')
        assert response.status_code == 200
