# Generated by Django 4.1.3 on 2022-11-30 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_cart_coupon_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyorder',
            name='updated_date',
            field=models.DateTimeField(),
        ),
    ]
