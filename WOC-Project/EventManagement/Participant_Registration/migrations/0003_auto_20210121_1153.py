# Generated by Django 3.1.5 on 2021-01-21 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Participant_Registration', '0002_auto_20210106_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='Contact_No',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='No_Of_Participant',
            field=models.PositiveIntegerField(),
        ),
    ]