# Generated by Django 4.2 on 2023-05-02 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='additonal_address',
            new_name='additional_address',
        ),
    ]