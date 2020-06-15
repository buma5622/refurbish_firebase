from django.shortcuts import render, redirect
from . forms import RegistratieForm, ReparatieForm
from . models import Computer


def computers(request):
    context = {'computers': Computer().all()}

    return render(request, 'computers.html', context)


def registratie(request):
    return render(request, 'registratie.html')


def post_registratie(request):
    computer = Computer()
    data = RegistratieForm.getData(request)
    computer.create(data)

    return redirect('computers')


def reparatie(request):
    context = {'computers': Computer().all()}

    return render(request, 'reparatie.html', context)


def reparatie_detail(request, id):
    context = {'computer': Computer().where('sku', id)}

    return render(request, 'reparatie_detail.html', context)


def post_reparatie(request, id):
    data = ReparatieForm.getData(request)
    print(data)
    Computer().update('sku', id, data)

    return redirect('reparatie')