# Generated by Django 3.1.5 on 2021-01-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=2000)),
                ('Location', models.CharField(max_length=100)),
                ('Link_of_Poster', models.URLField()),
                ('From_Date', models.DateField()),
                ('From_Time', models.TimeField()),
                ('To_Date', models.DateField()),
                ('To_Time', models.TimeField()),
                ('Dead_Date', models.DateField()),
                ('Dead_Time', models.TimeField()),
                ('Host_Name', models.CharField(max_length=100)),
                ('Host_Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
