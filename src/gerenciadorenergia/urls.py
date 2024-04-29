from django.urls import path
from . import views

app_name = 'gerenciadorenergia'
urlpatterns = [
    path('', view=views.index),
    path('cadastrar/', view=views.register),
    path('infos/', view=views.get_all),
    path('formated/', view=views.get_all_formated)
]
