# Generated by Django 4.1.3 on 2022-11-30 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_alter_historyorder_updated_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historyorder',
            old_name='updated_date',
            new_name='delivered_date',
        ),
    ]