# Generated by Django 4.2.6 on 2023-11-10 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]