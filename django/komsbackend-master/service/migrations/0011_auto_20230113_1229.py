# Generated by Django 3.2 on 2023-01-13 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_order_content_stationid'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatusName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderName', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='PreparationTime',
        ),
    ]
