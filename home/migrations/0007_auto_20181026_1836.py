# Generated by Django 2.0.8 on 2018-10-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20181026_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.FileField(max_length=255, upload_to=''),
        ),
    ]
