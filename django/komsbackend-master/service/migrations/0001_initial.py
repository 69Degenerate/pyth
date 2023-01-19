# Generated by Django 3.2 on 2023-01-07 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KOMS_config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('print_or_display', models.IntegerField()),
                ('default_prepration_time', models.CharField(max_length=20)),
                ('licence_key', models.CharField(max_length=200)),
                ('activation_status', models.IntegerField()),
                ('central_url', models.CharField(max_length=30)),
                ('send_order_to_cs', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu_sync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=False)),
                ('sync_mode', models.IntegerField()),
                ('sync_time', models.CharField(max_length=40)),
                ('sync_url', models.CharField(max_length=100)),
                ('provider', models.CharField(max_length=200)),
                ('sync_cred', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('externalOrderId', models.IntegerField()),
                ('pickupTime', models.CharField(max_length=90)),
                ('deliveryIsAsap', models.BooleanField(default=False)),
                ('arrival_time', models.CharField(max_length=30)),
                ('estimated_time', models.CharField(max_length=30)),
                ('order_status', models.IntegerField()),
                ('order_note', models.CharField(max_length=100)),
                ('order_type', models.IntegerField()),
                ('itemRemark', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Order_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('stationName', models.CharField(max_length=50)),
                ('quantityStatus', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
                ('note', models.CharField(max_length=50)),
                ('SKU', models.CharField(max_length=30)),
                ('tag', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.order')),
            ],
        ),
        migrations.CreateModel(
            name='Order_point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('activation_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Prepration_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('externalID', models.CharField(max_length=20)),
                ('tag', models.CharField(max_length=50)),
                ('prepration_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(max_length=50)),
                ('client_id', models.CharField(max_length=200)),
                ('client_secrete', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=20)),
                ('color_code', models.CharField(default=4281216584, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('staff_type', models.CharField(max_length=30)),
                ('active_status', models.IntegerField()),
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.stations')),
            ],
        ),
        migrations.CreateModel(
            name='Original_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderJSON', models.CharField(max_length=1000)),
                ('update_time', models.CharField(max_length=20)),
                ('externalOrderId', models.CharField(max_length=30)),
                ('parent', models.CharField(max_length=30)),
                ('orderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.order')),
            ],
        ),
        migrations.CreateModel(
            name='Order_point_cred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=500)),
                ('pointId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.order_point')),
            ],
        ),
        migrations.CreateModel(
            name='Order_modifer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantityStatus', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
                ('note', models.CharField(max_length=50)),
                ('SKU', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('contentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.order_content')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.order_point'),
        ),
        migrations.CreateModel(
            name='Modifer_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
                ('mod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.order_modifer')),
            ],
        ),
        migrations.CreateModel(
            name='Content_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(max_length=20)),
                ('contentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.order_content')),
            ],
        ),
        migrations.CreateModel(
            name='Content_assign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.order_content')),
                ('staffId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.staff')),
            ],
        ),
    ]
