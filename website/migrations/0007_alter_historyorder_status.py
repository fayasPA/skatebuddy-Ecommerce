# Generated by Django 4.1.3 on 2022-11-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_historyorder_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyorder',
            name='status',
            field=models.CharField(blank=True, choices=[('Order Palced', 'Order Palced'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='order palced', max_length=100, null=True),
        ),
    ]
