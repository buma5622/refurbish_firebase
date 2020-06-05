from django.shortcuts import render, redirect
from . forms import ComputerForms
from . models import Computer


def computers(request):
    context = {'computers': Computer().all()}

    return render(request, 'computers.html', context)


def registratie(request):
    return render(request, 'registratie.html')


def post_registratie(request):
    computer = Computer()
    data = ComputerForms.getData(request)
    computer.create(data)

    return redirect('computers')