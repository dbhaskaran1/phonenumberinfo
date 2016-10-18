from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, you've reached the info channel!")

def phone_number(request, phone_number):
    if phone_number:
        response = "This is the number you are requesting info on %s" % (phone_number)
    else:
        response = "No number received and one is expected for sure."

    return HttpResponse(response)
