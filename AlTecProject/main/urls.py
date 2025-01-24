from django.urls import path
from . import views
from .views import partners_page
from .views import views_about
from django.conf import settings
from django.conf.urls.static import static
from .views import faq_view
from .views import sendEmail

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('faq/', faq_view, name='faq'),
    path('partners/', partners_page, name='partners'),
    path('service/', views.service, name='service'),
    path('news/', views.news, name='news'),
    path('about/', views_about, name='about'),
    path('write/', views.write, name='write'),
    path('send-email/', sendEmail, name='send_email'),
    path('sertificate/', views.sertificate, name='sertificate'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


