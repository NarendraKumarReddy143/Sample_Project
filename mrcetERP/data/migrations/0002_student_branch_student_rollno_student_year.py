# Generated by Django 4.1.7 on 2024-03-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='branch',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]