# Generated by Django 3.2.2 on 2021-06-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prcjapp', '0009_auto_20210601_0935'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devicename', models.CharField(max_length=100)),
                ('item_id', models.CharField(max_length=100)),
                ('item_type', models.CharField(max_length=100)),
            ],
        ),
       
    ]
