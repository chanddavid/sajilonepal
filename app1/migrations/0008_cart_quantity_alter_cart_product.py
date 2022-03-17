# Generated by Django 4.0.3 on 2022-03-11 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
    ]
