from django.urls import path
from .views import partners_page
from .views import views_about
from django.conf import settings
from django.conf.urls.static import static
from .views import faq_view
from .views import sendEmail
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('faq/', faq_view, name='faq'),
    path('partners/', partners_page, name='partners'),
    path('service/', views.service, name='service'),
    path('service/<int:id_prod>/', views.service_detail, name='service_detail'),
    path('news/', views.news, name='news'),
    path('about/', views_about, name='about'),
    path('write/', views.write, name='write'),
    path('send-email/', sendEmail, name='send_email'),
    path('sertificate/', views.sertificate, name='sertificate'),
    path('search', views.search_page, name="search"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


