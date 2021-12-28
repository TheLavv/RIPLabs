from django.shortcuts import render
from lab5_app.models import Computer
from lab5_app.models import Browser


def get_comp_browsers_list(request):
    return render(request, 'comp_browsers.html', {
        'data': {
            'computers': Computer.objects.all(),
            'browsers': Browser.objects.all(),
        }
    })


def get_computer(request, id):
    return render(request, 'computer.html', {'data': {
        'computer': Computer.objects.filter(id=id)[0]
    }})


def get_browser(request, id):
    return render(request, 'browser.html', {'data': {
        'browser': Browser.objects.filter(id=id)[0],
        'computers': Computer.objects.all(),
    }})
