from django.urls import path
from . import views
from .views import partners_page
from .views import views_about

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('partners/', partners_page, name='partners'),
    path('service/', views.service, name='service'),
    path('news/', views.news, name='news'),
    path('about/', views_about, name='about'),
    path('write/', views.write, name='write'),
    path('sertificate/', views.sertificate, name='sertificate'),
]


