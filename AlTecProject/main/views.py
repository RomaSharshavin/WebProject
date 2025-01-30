from .models import News
from .models import FAQ
import requests
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Service

from django.db.models import Q
import os
import re
from django.conf import settings
from bs4 import BeautifulSoup
import json


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
    page_numbers = list(range(1, total_pages + 1))  # Create a list of page numbers

    return render(request, 'main/faq.html', {
        'faqs': page_obj,
        'total_pages': total_pages,
        'current_page': current_page,
        'page_numbers': page_numbers,  # Pass the list of page numbers to the template
    })

def partners(request):
    return render(request, 'main/partners.html')


def service(request):
    services = Service.objects.all()

    # Сопоставление категорий с id_prod
    category_map = {
        'subcategory1': [1, 2, 3, 4, 5, 6],
        'subcategory2': [7],
        'subcategory3': [8],
        'subcategory4': [9],
        'subcategory5': [10, 11],
        'subcategory6': [12],
        'subcategory7': [13],
    }

    category_id = request.GET.get('category')  # Получаем id категории из запроса
    if category_id and category_id in category_map:
        services = services.filter(id_prod__in=category_map[category_id])  # Фильтруем по id_prod

    paginator = Paginator(services, 3)  # Указываем количество сервисов на странице
    current_page = int(request.GET.get('page', 1))
    page_obj = paginator.get_page(current_page)

    total_pages = paginator.num_pages
    pages = list(range(1, total_pages + 1))  # Создаем список страниц

    return render(request, 'main/service.html', {
        'services': page_obj,
        'total_pages': total_pages,
        'current_page': current_page,
        'pages': pages,  # Передаем список страниц в шаблон
        'category_id': category_id,  # Передаем id категории
    })


def service_detail(request, id_prod):
    service = get_object_or_404(Service, id_prod=id_prod)
    # Убираем табуляции и заменяем их на пробелы
    cleaned_text = service.characteristics.replace('\t', ' ').strip()

    # Разделяем по символу |
    characteristics_list = [
        line.strip() for line in cleaned_text.split('|') if line.strip()
    ]

    return render(request, 'main/service_detail.html', {
        'service': service,
        'characteristics': characteristics_list
    })


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


def search_page(request):
    query = request.GET.get('search', '').strip()
    page_number = request.GET.get('page', 1)

    all_results = []  # Список для объединения всех результатов

    if query:
        # Поиск в моделях базы данных
        news_results = News.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        service_results = Service.objects.filter(
            Q(prod_name__icontains=query) | Q(description__icontains=query) | Q(characteristics__icontains=query)
        )
        faq_results = FAQ.objects.filter(Q(question__icontains=query) | Q(answer__icontains=query))
        html_results = search_in_static_html(query)

        all_results.extend(news_results)
        all_results.extend(service_results)
        all_results.extend(faq_results)
        all_results.extend(html_results)

    # Пагинация для всех результатов
    paginator = Paginator(all_results, 3)  # Ограничение до 4 блоков
    current_page = paginator.get_page(page_number)

    return render(request, 'main/search.html', {
        'query': query,
        'results': current_page,  # Все результаты в одной переменной
        'total_pages': paginator.num_pages,
        'current_page': page_number,
        'page_numbers': range(1, paginator.num_pages + 1),
    })


def search_in_static_html(query):
    """Поиск текста в статических HTML-страницах и вывод нужного фрагмента"""
    html_results = []
    static_dir = os.path.join(settings.BASE_DIR, 'main/templates/main')  # HTML-файлы
    titles_path = os.path.join(settings.BASE_DIR, 'main/static/images/json/titles.json')  # Путь к JSON

    # Загружаем заголовки из JSON
    try:
        with open(titles_path, 'r', encoding='utf-8') as f:
            page_titles = json.load(f)
    except FileNotFoundError:
        page_titles = {}

    for file_name in os.listdir(static_dir):
        if file_name.endswith('.html'):
            file_path = os.path.join(static_dir, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

                # Используем BeautifulSoup для извлечения текста
                soup = BeautifulSoup(content, 'html.parser')

                # Оставляем только текст из заголовков и параграфов
                visible_text = ' '.join(tag.get_text(" ", strip=True) for tag in
                                        soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong', 'td', 'th', 'label']))

                # Получаем заголовок только из JSON
                page_title = page_titles.get(file_name, file_name.replace('.html', ''))

                # Регулярное выражение для поиска слова + 50 символов до и после
                matches = re.findall(rf'(.{{0,50}}{re.escape(query)}.{{0,50}})', visible_text, re.IGNORECASE)

                if matches:
                    html_results.append({
                        'page_title': page_title,
                        'matches': matches,
                        'url': f'/{file_name.replace(".html", "")}/'
                    })
    return html_results