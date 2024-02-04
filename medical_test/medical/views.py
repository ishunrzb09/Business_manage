import platform

from django.shortcuts import HttpResponse, render

# Create your views here.


def welcome_call(request):
    return HttpResponse(
        f"Welcome to docker and k8s training session your container id is <strong>{platform.node()}<strong/>"
    )


def hello(request):

    return HttpResponse(f"this is test project for medical application")
