# Generated by Django 3.0.8 on 2020-08-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='mooBlog', max_length=255),
        ),
    ]
