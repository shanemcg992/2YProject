# Generated by Django 4.0.3 on 2022-03-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlistitem',
            old_name='Watchlist',
            new_name='watchlist',
        ),
        migrations.AddField(
            model_name='watchlistitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
