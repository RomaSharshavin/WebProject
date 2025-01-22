from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News
from .models import FAQ


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'main/faq.html', {'faqs': faqs})


def partners(request):
    return render(request, 'main/partners.html')


def service(request):
    return render(request, 'main/service.html')


def sertificate(request):
    return render(request, 'main/sertificate.html')


def write(request):
    return render(request, 'main/write.html')


def news(request):
    news_list = News.objects.order_by('-date_written')  # Сортировка по датеё
    paginator = Paginator(news_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'main/news.html', {'page_obj': page_obj})


def about(request):
    return render(request, 'main/about.html')


def format_text(text):
    paragraphs = text.split('\n\n')  # Разделяем текст на абзацы
    return ''.join(f'<p>{paragraph.strip()}</p>' for paragraph in paragraphs)


def partners_page(request):
    return render(request, 'main/partners.html')


def views_about(request):
    return render(request, 'main/about.html')
