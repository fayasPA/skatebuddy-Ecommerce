# Generated by Django 4.1.3 on 2022-11-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_cart_discounted_amnt'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
