from django.shortcuts import render
from .models import News


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


def faq(request):
    return render(request, 'main/faq.html')


def production(request):
    return render(request, 'main/production.html')


def service(request):
    return render(request, 'main/service.html')


def sertificate(request):
    return render(request, 'main/sertificate.html')


def write(request):
    return render(request, 'main/write.html')


def news(request):
    news_items = News.objects.all()
    return render(request, 'main/news.html', {'news_items': news_items})


def about(request):
    return render(request, 'main/about.html')
