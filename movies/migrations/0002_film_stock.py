# Generated by Django 4.0.3 on 2022-03-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='stock',
            field=models.IntegerField(default=1000),
        ),
    ]
