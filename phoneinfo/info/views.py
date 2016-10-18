from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from models import PhoneInfo
from lib import phone_info

def index(request):
    return HttpResponse("Hello, you've reached the info channel!")

def phone_number(request, phone_number):
    if phone_number:
        response = "This is the number you are requesting info on %s" % (phone_number)
        rs = PhoneInfo.objects.filter(phone_number = phone_number)
        number = phone_info.PhoneNumber(phone_number, 'US')
        try:
            result = number.get_data()
            context = {
                'value': phone_number,
                'is_number_valid': result['is_number_valid']
            }
            return render(request, 'info/index.html', context)
        except Exception as e:
            response = "Bad number received." + str(e)
            return HttpResponse(response)


    else:
        response = "No number received and one is expected for sure."
        return HttpResponse(response)

