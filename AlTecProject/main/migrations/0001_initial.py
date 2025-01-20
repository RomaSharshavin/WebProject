# Generated by Django 5.1.1 on 2025-01-20 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Новость')),
                ('text', models.TextField(max_length=400, verbose_name='Описание')),
                ('date_written', models.DateTimeField(auto_now_add=True, verbose_name='Дата написания')),
            ],
        ),
    ]
