from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from models import PhoneInfo

def index(request):
    return HttpResponse("Hello, you've reached the info channel!")

def phone_number(request, phone_number):
    if phone_number:
        response = "This is the number you are requesting info on %s" % (phone_number)
        rs = PhoneInfo.objects.filter(phone_number = phone_number)
        context = {
            'value': phone_number,
            'count': rs.count(),
        }
        return render(request, 'info/index.html', context)
    else:
        response = "No number received and one is expected for sure."
        return HttpResponse(response)

