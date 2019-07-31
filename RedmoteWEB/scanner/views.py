from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context = {'devices': [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}]}
    return render(request, 'scanner/device-list.html', context)