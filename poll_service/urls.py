from django.contrib import admin
from django.urls import path
from poll_service import http_handler

urlpatterns = [
    path('answer', http_handler.answer , name='answer'),
    path('answer/<str:poll_id>', http_handler.answers_for_poll, name="answer_for_poll"),
    path('poll', http_handler.poll , name='poll'),
    path('poll/<str:poll_id>', http_handler.poll_id , name='poll_id'),
    path('checkAnswer/<str:user_id>/<str:poll_id>', http_handler.check_answer, name='checkAnswer')
]
