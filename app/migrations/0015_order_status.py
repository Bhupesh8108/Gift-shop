# Generated by Django 4.1.7 on 2023-05-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_search_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('arriving', 'arriving'), ('delivered', 'delivered'), ('pending', 'pending')], default='pending', max_length=10),
        ),
    ]
