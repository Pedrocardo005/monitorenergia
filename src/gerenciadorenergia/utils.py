from django.db.models.query import QuerySet
from gerenciadorenergia.models import InfoConsumo
from django.utils import timezone
from datetime import datetime

class Utils:

    @staticmethod
    def get_list_consumo(results: QuerySet[InfoConsumo], count_filter: int, type_time: str):
        listing = {}
        listing['items'] = []
        count = results.count()

        if count > 10:
            device = { 'consumo': 0 }
            _cont = 0
            for idx, result in enumerate(results):
                _cont += 1
                device['consumo'] += result.consumo
                ['M', 'H', 'd']

                if _cont >= count_filter:
                    device['consumo'] /= count_filter
                    device['nome'] = result.nome_dispositivo
                    device['tempo'] = Utils.between_two_dates(result.date_time, type_time)
                    listing['items'].append(device.copy())
                    _cont = 0
                    device['nome'] = ''
                    device['consumo'] = 0
                elif count - 1 == idx:
                    device['consumo'] /= count % count_filter
                    device['nome'] = result.nome_dispositivo
                    device['tempo'] = Utils.between_two_dates(result.date_time, type_time)
                    listing['items'].append(device.copy())
        else:
            for idx, result in enumerate(results):
                device = {}
                device['consumo'] = result.consumo
                device['nome'] = result.nome_dispositivo
                device['tempo'] = Utils.between_two_dates(result.date_time, type_time)
                listing['items'].append(device.copy())

        return listing
    

    @staticmethod
    def between_two_dates(initial_time: datetime, type_time: str):
        difference = timezone.now() - initial_time

        if type_time == 'M':
            return int(difference.total_seconds() / 60)
        if type_time == 'H':
            return int(difference.total_seconds() / 3600)
        if type_time == 'd':
            return int(difference.total_seconds() / 86400)
        else:
            return int(difference.total_seconds())
