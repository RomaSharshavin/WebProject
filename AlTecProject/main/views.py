from django.http import Http404
from django.shortcuts import render
import os


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


def faq(request):
    return render(request, 'main/faq.html')


def partners(request):
    return render(request, 'main/partners.html')


def service(request):
    return render(request, 'main/service.html')


def sertificate(request):
    return render(request, 'main/sertificate.html')


def write(request):
    return render(request, 'main/write.html')


def news(request):
    return render(request, 'main/news.html')


def about(request):
    return render(request, 'main/about.html')


def format_text(text):
    paragraphs = text.split('\n\n')  # Разделяем текст на абзацы
    return ''.join(f'<p>{paragraph.strip()}</p>' for paragraph in paragraphs)


def partners_page(request):
    texts_dir = "media/texts"
    texts = []

    for i in range(2, 4):  # Загружаем только text2.txt и text3.txt
        file_path = os.path.join(texts_dir, f"text{i}.txt")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                formatted_content = format_text(content)
                texts.append(formatted_content)
        except FileNotFoundError:
            print(f"Файл не найден: {file_path}")
            texts.append(f"<p>Файл text{i}.txt не найден.</p>")

    if not texts:  # Проверяем, если texts пусто
        raise Http404("Нет текстов для отображения.")

    return render(request, 'main/partners.html', {'texts': texts})

def views_about(request):
    texts_dir = "media/texts"
    file_name = "text4.txt"  # Укажите конкретный файл
    file_path = os.path.join(texts_dir, file_name)
    texts = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            formatted_content = format_text(content)
            texts.append(formatted_content)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        texts.append(f"<p>Файл {file_name} не найден.</p>")

    if not texts:  # Проверяем, если texts пусто
        raise Http404("Нет текстов для отображения.")

    return render(request, 'main/about.html', {'texts': texts})