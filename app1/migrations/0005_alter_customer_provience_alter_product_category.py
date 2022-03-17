# Generated by Django 4.0.3 on 2022-03-10 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='provience',
            field=models.CharField(choices=[('Provience_1', 'Provience_1'), ('Provience_2', 'Provience_2'), ('Provience_3', 'Provience_3'), ('Provience_4', 'Provience_4'), ('Provience_5', 'Provience_5'), ('Gandaki', 'Gandaki'), ('Sudurpaschim', 'Sudurpaschim')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'mobile'), ('C', 'camera'), ('T', 'tshirt'), ('HP', 'headphone')], max_length=2),
        ),
    ]
