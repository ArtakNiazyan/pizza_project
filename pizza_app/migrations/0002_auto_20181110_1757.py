# Generated by Django 2.1.3 on 2018-11-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
