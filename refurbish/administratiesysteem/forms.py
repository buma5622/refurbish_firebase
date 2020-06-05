from datetime import datetime
from . models import Computer


class ComputerForms:

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