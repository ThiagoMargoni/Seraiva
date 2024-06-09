# Generated by Django 5.0.5 on 2024-06-06 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('refused', 'refused')], default='pending', max_length=50),
        ),
    ]
