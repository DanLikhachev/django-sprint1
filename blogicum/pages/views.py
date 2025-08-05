from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.


def about(request: HttpRequest) -> HttpResponse:
    """Обработка запроса about."""
    template_name = 'pages/about.html'
    return render(request, template_name)


def rules(request: HttpRequest) -> HttpResponse:
    """Обработка запроса rules."""
    template_name = 'pages/rules.html'
    return render(request, template_name)
