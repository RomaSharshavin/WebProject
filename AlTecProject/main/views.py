from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News
from .models import FAQ
from django import template

from django.core.mail import send_mail
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


def faq_view(request):
    faqs = FAQ.objects.all()
    paginator = Paginator(faqs, 5)  # 5 questions per page
    page_number = request.GET.get('page')
    faqs_page = paginator.get_page(page_number)

    # Create a list of page numbers
    page_numbers = list(range(1, paginator.num_pages + 1))

    return render(request, 'main/faq.html',
                  {'faqs': faqs_page, 'page_numbers': page_numbers, 'total_faqs': paginator.count})


def partners(request):
    return render(request, 'main/partners.html')


def service(request):
    return render(request, 'main/service.html')


def sertificate(request):
    return render(request, 'main/sertificate.html')


def write(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        question = request.POST.get('question')

        message = f"Имя: {name}\nТелефон: {phone}\nEmail: {email}\nВопрос: {question}"

        try:
            send_mail(
                subject="Новое сообщение с сайта",
                message=message,
                from_email='your_email@example.com',  # Ваш email
                recipient_list=['recipient_email@example.com'],  # Кому отправить
                fail_silently=False,
            )
        except Exception as e:
            return HttpResponse(f"Ошибка отправки сообщения: {e}")

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
