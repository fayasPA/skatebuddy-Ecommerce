# Generated by Django 4.1.3 on 2022-11-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_historyorder_updated_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyorder',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
