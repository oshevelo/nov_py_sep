# Generated by Django 2.2.4 on 2020-02-24 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20200224_1030'),
        ('products', '0005_auto_20200127_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalogue.Category'),
        ),
    ]
