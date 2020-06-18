from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotAllowed
# Create your views here.


def ok(request):
    if request.method == 'GET':
        return HttpResponse(status=200)
    elif request.method == 'POST':
        return HttpResponse(status=405)
    elif request.method == 'PUT':
        return HttpResponse(status=405)


def slug_route(request: HttpRequest, title):
    return HttpResponse(title)


def sum(request: HttpRequest, n1, n2):
    return HttpResponse(n1 + n2)


def sum_get_method(request: HttpRequest):
    if request.method == 'GET':
        a = request.GET.get('a', '')
        b = request.GET.get('b', '')
        try:
            return HttpResponse(int(a) + int(b))
        except ValueError:
            return HttpResponse(status=400)
    return HttpResponseNotAllowed('GET')


def sum_post_method(request: HttpRequest):
    if request.method == 'POST':
        a = request.POST.get('a', '')
        b = request.POST.get('b', '')
        try:
            return HttpResponse(int(a) + int(b))
        except ValueError:
            return HttpResponse(status=400)
    return HttpResponseNotAllowed('POST')
