# Generated by Django 3.0.2 on 2020-01-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=50)),
                ('num1', models.IntegerField()),
                ('num2', models.IntegerField()),
                ('result', models.IntegerField()),
            ],
        ),
    ]
