# Procedimentos recomendados ao atualizar algum pacote

 - Atualize a listagem dos pacotes no requirements.txt por meio do comando ```pip freeze > requirements.txt```

 ## Erros reconhecidos durante o deploy no Python anywhere

Caso o comando ```python manage.py collectstatic``` não funcionar, tente isso ```export DJANGO_SETTINGS_MODULE=monitorenergia.settings.pythonanywhere```
