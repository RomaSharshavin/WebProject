from django.urls import path
from . import views

app_name = 'write'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('production/', views.production, name='production'),
    path('service/', views.service, name='service'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('write/', views.write, name='write'),
    path('sertificate/', views.sertificate, name='sertificate'),
]