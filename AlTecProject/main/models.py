from django.db import models


class News(models.Model):
    title = models.CharField('Новость', max_length=50)
    text = models.TextField('Описание', max_length=400)
    date_written = models.DateTimeField('Дата написания', auto_now_add=True)

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=400)

    def __str__(self):
        return self.question


class Service(models.Model):
    id_prod = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=255)
    image_path = models.URLField()
    description = models.TextField()
    characteristics = models.TextField()

    def __str__(self):
        return self.prod_name
