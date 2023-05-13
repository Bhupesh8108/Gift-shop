# Generated by Django 4.2 on 2023-05-13 05:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 13, 5, 41, 10, 5087, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
