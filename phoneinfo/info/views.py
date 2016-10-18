from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse, JsonResponse
from models import PhoneInfo
from lib import phone_info, current_datetime

def index(request):
    return JsonResponse({"message": "Hello, you've reached the index. No info here!"})

def phone_number(request, phone_number, country_code = 'US'):
    if phone_number:
        rs = PhoneInfo.objects.filter(phone_number = phone_number)
        number = phone_info.PhoneNumber(phone_number, country_code)
        try:
            result = number.get_data()
            return JsonResponse(result)
        except Exception as e:
            result = {}
            result['error'] = "Error occurred." + str(e)
            return JsonResponse(result)
    else:
        result = {}
        result['error'] = "No number received and one is expected for sure."
        return JsonResponse(result)

def get_date(request):
    result = current_datetime.get_current_date()
    return JsonResponse(result)

def get_time(request):
    result = current_datetime.get_current_time()
    return JsonResponse(result)
