# Generated by Django 4.2.10 on 2024-02-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metals', '0003_alter_metal_element_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metal',
            name='element_symbol',
            field=models.TextField(verbose_name='unknown'),
        ),
    ]
