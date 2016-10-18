from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from models import PhoneInfo
from lib import phone_info

def index(request):
    return HttpResponse("Hello, you've reached the info channel!")

def phone_number(request, phone_number, country_code = 'US'):
    if phone_number:
        rs = PhoneInfo.objects.filter(phone_number = phone_number)
        number = phone_info.PhoneNumber(phone_number, country_code)
        try:
            result = number.get_data()
            context = {
                'result': result
            }
            return render(request, 'info/index.html', context)
        except Exception as e:
            response = "Error occurred." + str(e)
            return HttpResponse(response)


    else:
        response = "No number received and one is expected for sure."
        return HttpResponse(response)

