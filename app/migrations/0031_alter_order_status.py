# Generated by Django 4.2 on 2023-05-19 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_item_active_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Accepted', 'Accepted')], default='Pending', max_length=10),
        ),
    ]
