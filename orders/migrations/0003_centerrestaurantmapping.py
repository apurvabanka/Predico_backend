# Generated by Django 3.0.2 on 2020-04-29 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderdetails_center_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='centerRestaurantMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_id', models.IntegerField()),
                ('restaurant_id', models.IntegerField()),
            ],
        ),
    ]