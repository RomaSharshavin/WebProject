from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News
from .models import FAQ
from django import template
import requests
from django.http import JsonResponse
from django.core.mail import send_mail
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


from django.core.paginator import Paginator


def faq_view(request):
    faqs = FAQ.objects.all()  # Получаем все записи FAQ
    paginator = Paginator(faqs, 5)  # 5 на страницу
    current_page = int(request.GET.get('page', 1))  # Преобразуем в целое число
    page_obj = paginator.get_page(current_page)

    total_pages = paginator.num_pages

    return render(request, 'main/faq.html', {
        'faqs': page_obj,
        'total_pages': total_pages,
        'current_page': current_page,  # Отправляем как целое
    })

def partners(request):
    return render(request, 'main/partners.html')


def service(request):
    return render(request, 'main/service.html')


def sertificate(request):
    return render(request, 'main/sertificate.html')


def write(request):
    return render(request, 'main/write.html')

def sendEmail(request):
    if request.method == 'POST':
        # Получите данные из формы
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        question = request.POST['question']
        recaptcha_response = request.POST['g-recaptcha-response']

        # Проверка reCAPTCHA
        secret_key = '6LeeccIqAAAAANIAHfpRG9Hz4UKUlkVRked0oruU'  # Замените своим Secret Key
        data = {
            'secret': secret_key,
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()

        if result.get('success'):
            # Здесь ваш код для отправки email...
            return JsonResponse({'status': 'success', 'message': 'Сообщение успешно отправлено!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Проверка reCAPTCHA не пройдена!'})
    return JsonResponse({'status': 'error', 'message': 'Некорректный запрос!'})

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
