# Generated by Django 4.2.1 on 2023-06-04 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_customers_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='promotions',
            field=models.ManyToManyField(to='store.promotion'),
        ),
    ]
