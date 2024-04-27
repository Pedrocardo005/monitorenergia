# Procedimentos recomendados ao atualizar algum pacote

 - Atualize a listagem dos pacotes no requirements.txt por meio do comando ```pip freeze > requirements.txt```

 ## Erros reconhecidos

Caso o comando ```python manage.py collectstatic```, ou qualquer do python + django não funcionar, tente isso antes ```export DJANGO_SETTINGS_MODULE=monitorenergia.settings.pythonanywhere```

Não se esqueça de adicionar a url da pasta com os statics na aba **Static files** da página do webapp
