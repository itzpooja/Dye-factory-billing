# Generated by Django 3.0.3 on 2020-03-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20200313_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mt_type',
            name='mt_price',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True),
        ),
    ]