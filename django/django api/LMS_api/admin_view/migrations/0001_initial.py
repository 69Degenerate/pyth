# Generated by Django 4.1 on 2022-10-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=200)),
                ('book_author', models.CharField(max_length=100)),
                ('book_pages', models.CharField(max_length=50)),
                ('book_avail', models.CharField(choices=[('AVAILABLE', 'available'), ('UNAVAILABLE', 'unavailable')], default='unavailable', max_length=20)),
            ],
        ),
    ]
