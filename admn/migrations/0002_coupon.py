# Generated by Django 4.1.3 on 2022-11-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
