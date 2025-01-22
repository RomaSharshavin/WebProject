from django.contrib import admin
from .models import News
from .models import FAQ

# Register your models here.

admin.site.register(News)

admin.site.register(FAQ)
