from django.db.models.aggregates import Sum
from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Computer, Browser
from django.db import models


def index(request):
    return render(request, 'index.html')


# BROWSERS


def read_browser(request):
    browsers = Browser.objects.all()
    return render(request, 'browser/browser_list.html', {'browsers': browsers})


def create_browser(request):
    if request.method == 'GET':
        comp_browsers = Computer.objects.all()
        return render(request, 'browser/create_browser.html', {"comp_browsers": comp_browsers})
    else:
        dto = {}
        for key in request.POST:
            if key in Browser.__dict__:
                dto[key] = request.POST[key]
        dto['comp_browser'] = get_object_or_404(Computer, pk=request.POST['comp_browser'])
        new_browser = Browser(**dto)
        new_browser.save()
        return redirect('read_browser')


def update_browser(request, browser_id):
    if request.method == 'GET':
        comp_browsers = Computer.objects.all()
        browser = get_object_or_404(Browser, pk=browser_id)
        return render(request, 'browser/update_browser.html', {"browser": browser, "comp_browsers": comp_browsers})
    else:
        browser = get_object_or_404(Browser, pk=browser_id)
        for key in request.POST:
            if key in browser.__dict__ and key != 'comp_browser':
                setattr(browser, key, request.POST[key])
        if 'comp_browser' in request.POST:
            setattr(browser, 'comp_browser', get_object_or_404(
                Computer, pk=request.POST['comp_browser']))
        browser.save()
        return redirect('read_browser')


def delete_browser(request, browser_id):
    browser = get_object_or_404(Browser, pk=browser_id)
    browser.delete()
    return redirect(request.META.get('HTTP_REFERER'))


# COMPUTER BROWSERS


def read_comp_browser(request):
    comp_browsers = Computer.objects.all()
    return render(request, 'comp_browser/comp_browser_list.html', {'comp_browsers': comp_browsers})


def create_comp_browser(request):
    if request.method == 'GET':
        return render(request, 'comp_browser/create_comp_browser.html')
    else:
        dto = {}
        for key in request.POST:
            if key in Computer.__dict__:
                dto[key] = request.POST[key]
        new_comp_browser = Computer(**dto)
        new_comp_browser.save()
        return redirect('read_comp_browser')


def update_comp_browser(request, comp_browser_id):
    if request.method == 'GET':
        comp_browser = get_object_or_404(Computer, pk=comp_browser_id)
        return render(request, 'comp_browser/update_comp_browser.html', {"comp_browser": comp_browser})
    else:
        comp_browser = get_object_or_404(Computer, pk=comp_browser_id)
        for key in request.POST:
            if key in comp_browser.__dict__:
                setattr(comp_browser, key, request.POST[key])
        comp_browser.save()
        return redirect('read_comp_browser')


def delete_comp_browser(request, comp_browser_id):
    comp_browser = get_object_or_404(Computer, pk=comp_browser_id)
    comp_browser.delete()
    return redirect(request.META.get('HTTP_REFERER'))


# REPORT


def report(request):
    sorted_computers = Computer.objects.order_by("name")
    memory_on_disk_arr = []
    for comp_browser in Computer.objects.all():
        browsers_on_comp = Browser.objects.filter(comp_browser=comp_browser.pk)
        if len(browsers_on_comp) != 0:
            memory_on_disk_arr.append({"comp_browser": comp_browser, "memory_on_disk": Browser.objects.filter(
                comp_browser=comp_browser.pk).aggregate(Sum('memory_on_disk'))['memory_on_disk__sum']})
    return render(request, 'report.html', {"sorted_computers": sorted_computers,
                                           "memory_on_disk_arr": sorted(memory_on_disk_arr,
                                                                        key=lambda A: -1 * A['memory_on_disk'])})
