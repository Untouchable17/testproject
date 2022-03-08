# Generated by Django 4.0.3 on 2022-03-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Пост')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
