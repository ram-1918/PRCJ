# Generated by Django 4.1.5 on 2023-01-30 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetails",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="map_product",
                to="products.price",
            ),
        ),
        migrations.AlterField(
            model_name="orders",
            name="products",
            field=models.ManyToManyField(
                through="orders.OrderDetails", to="products.price"
            ),
        ),
    ]
