from django.shortcuts import render
from .models import News
from .models import FAQ
import requests
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Service

def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


def faq_view(request):
    faqs = FAQ.objects.all()
    paginator = Paginator(faqs, 5)
    current_page = int(request.GET.get('page', 1))
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
    services = Service.objects.all()
    paginator = Paginator(services, 2)
    current_page = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(current_page)

    total_pages = paginator.num_pages

    return render(request, 'main/service.html', {
        'services': page_obj,
        'total_pages': total_pages,
        'current_page': current_page,  # Отправляем как целое
    })


def service_detail(request, id_prod):
    service = get_object_or_404(Service, id_prod=id_prod)
    return render(request, 'main/service_detail.html', {'service': service})


def sertificate(request):
    return render(request, 'main/sertificate.html')


def write(request):
    return render(request, 'main/write.html')


def sendEmail(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        question = request.POST['question']
        recaptcha_response = request.POST['g-recaptcha-response']

        # Проверка reCAPTCHA
        secret_key = '6LeeccIqAAAAANIAHfpRG9Hz4UKUlkVRked0oruU'
        data = {
            'secret': secret_key,
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = response.json()

        if result.get('success'):
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
    paragraphs = text.split('\n\n')
    return ''.join(f'<p>{paragraph.strip()}</p>' for paragraph in paragraphs)


def partners_page(request):
    return render(request, 'main/partners.html')


def views_about(request):
    return render(request, 'main/about.html')
