# Generated by Django 4.1.5 on 2023-01-10 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0009_orderitem_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_cart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='LittleLemonDRF.cart'),
        ),
    ]