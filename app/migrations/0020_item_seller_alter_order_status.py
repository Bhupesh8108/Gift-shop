# Generated by Django 4.2 on 2023-05-13 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0019_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(default='26', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
    ]
