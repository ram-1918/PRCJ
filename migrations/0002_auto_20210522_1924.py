# Generated by Django 3.2.2 on 2021-05-22 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prcjapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='harammodels',
            old_name='haramcode',
            new_name='haram_id',
        ),
        migrations.RenameField(
            model_name='harammodels',
            old_name='haramimg',
            new_name='haram_image',
        ),
        migrations.RenameField(
            model_name='harammodels',
            old_name='haramweight',
            new_name='haram_weight',
        ),
    ]