from django.contrib import admin
from django.urls import path
from poll_service import http_handler

urlpatterns = [
    path('answer', http_handler.answer , name='answer'),
    path('poll', http_handler.answer , name='poll'),
]
