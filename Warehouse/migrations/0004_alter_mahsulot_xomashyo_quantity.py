# Generated by Django 5.0.3 on 2024-03-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Warehouse', '0003_alter_mahsulot_xomashyo_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot_xomashyo',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]