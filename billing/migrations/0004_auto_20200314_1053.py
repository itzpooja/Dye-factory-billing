# Generated by Django 3.0.3 on 2020-03-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_auto_20200314_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='received_details',
            name='dc_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='received_details',
            name='m_length',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
