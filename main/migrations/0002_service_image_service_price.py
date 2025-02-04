# Generated by Django 5.1.1 on 2025-01-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services/'),
        ),
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
