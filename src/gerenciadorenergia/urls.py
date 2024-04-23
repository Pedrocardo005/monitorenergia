from django.urls import path
from . import views

app_name = 'gerenciadorenergia'
urlpatterns = [
    path('', view=views.index),
    path('cadastrar/', view=views.register)
]
