from django.contrib import admin
from django.urls import include, path
from medical import views

urlpatterns = [
    path('v1/', views.welcome_call),
    path('hello/', views.hello)
]