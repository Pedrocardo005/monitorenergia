from django.db.models.query import QuerySet
from gerenciadorenergia.models import InfoConsumo

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

                if _cont >= count_filter:
                    device['consumo'] /= count_filter
                    device['nome'] = result.nome_dispositivo
                    device['tempo'] = result.date_time.strftime("%" + type_time)
                    listing['items'].append(device.copy())
                    _cont = 0
                    device['nome'] = ''
                    device['consumo'] = 0
                elif count - 1 == idx:
                    device['consumo'] /= count % count_filter
                    device['nome'] = result.nome_dispositivo
                    device['tempo'] = result.date_time.strftime("%" + type_time)
                    listing['items'].append(device.copy())
        else:
            for idx, result in enumerate(results):
                device = {}
                device['consumo'] = result.consumo
                device['nome'] = result.nome_dispositivo
                device['tempo'] = result.date_time.strftime("%" + type_time)
                listing['items'].append(device.copy())

        return listing