# Generated by Django 4.0.2 on 2022-02-19 13:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='genre')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='film')),
                ('available', models.BooleanField(default=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
            options={
                'verbose_name': 'film',
                'verbose_name_plural': 'films',
                'ordering': ('name',),
            },
        ),
    ]