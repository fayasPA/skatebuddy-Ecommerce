# Generated by Django 4.1.3 on 2022-11-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_historyorder_coupon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discounted_amnt',
            field=models.FloatField(default=0.0),
        ),
    ]
