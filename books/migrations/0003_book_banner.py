# Generated by Django 5.0.4 on 2024-05-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='banner',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]
