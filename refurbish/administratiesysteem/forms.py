from datetime import datetime
from . models import Computer


class RegistratieForm:

    @classmethod
    def getData(cls, request):
        computer = Computer()

        data = {
            'sku': computer.primary_key('sku'),
            'dag': datetime.now().day,
            'maand': datetime.now().month,
            'jaar': datetime.now().year,
        }

        for key, value in request.POST.items():
            data[key] = value

        return data


class ReparatieForm:

    @classmethod
    def getData(cls, request):
        computer = Computer()

        data = {
            'afbeelding': str(request.FILES['afbeelding']),
        }

        for key, value in request.POST.items():
            data[key] = value

        return data