from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('partners/', views.partners_page, name='partners'),
    path('service/', views.service, name='service'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('write/', views.write, name='write'),
    path('sertificate/', views.sertificate, name='sertificate'),
]


