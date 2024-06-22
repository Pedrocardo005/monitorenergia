from django.urls import path
from . import views

app_name = 'gerenciadorenergia'
urlpatterns = [
    path('', view=views.index),
    path('cadastrar/', view=views.register),
    path('infos/', view=views.get_all),
    path('formated/minute/', view=views.get_all_by_minute),
    path('formated/hour/', view=views.get_all_by_hour),
    path('formated/day/', view=views.get_all_by_day),
    path('formated/week/', view=views.get_all_by_week),
    path('send/arduino', view=views.to_send_arduino_information),
]
