# Generated by Django 3.2.2 on 2021-06-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prcjapp', '0010_auto_20210601_1058'),
    ]

    operations = [

        migrations.AddField(
            model_name='wishlist',
            name='item_status',
            field=models.BooleanField(default=False),
        ),
    ]
