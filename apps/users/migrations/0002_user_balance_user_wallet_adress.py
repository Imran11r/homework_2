# Generated by Django 5.0.1 on 2024-01-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.IntegerField(blank=True, default=4, null=True, verbose_name='Баланс'),
        ),
        migrations.AddField(
            model_name='user',
            name='wallet_adress',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True, verbose_name='Кошелек'),
        ),
    ]