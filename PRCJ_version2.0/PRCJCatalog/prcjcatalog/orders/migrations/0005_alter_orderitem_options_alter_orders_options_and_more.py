# Generated by Django 4.1.5 on 2023-01-31 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_users_options"),
        ("products", "0004_alter_goldprice_options_alter_price_options_and_more"),
        ("orders", "0004_rename_account_orders_users_remove_orderitem_price_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="orderitem",
            options={"verbose_name_plural": "OrderItem"},
        ),
        migrations.AlterModelOptions(
            name="orders",
            options={"verbose_name_plural": "Orders"},
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orderitem",
                to="orders.orders",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orderitem",
                to="products.price",
            ),
        ),
        migrations.AlterField(
            model_name="orders",
            name="users",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="users.users",
            ),
        ),
    ]
