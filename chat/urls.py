from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', ChatView.as_view(), name="chat")
]