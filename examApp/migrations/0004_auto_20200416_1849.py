# Generated by Django 2.0 on 2020-04-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examApp', '0003_article_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
