# Generated by Django 2.0 on 2020-04-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('examApp', '0002_delete_human'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
                ('description', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='')),
                ('text', models.TextField()),
                ('time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('time', models.DateTimeField()),
            ],
        ),
    ]