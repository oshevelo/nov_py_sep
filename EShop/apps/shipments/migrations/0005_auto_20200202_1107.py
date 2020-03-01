# Generated by Django 2.2.4 on 2020-02-02 11:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0004_merge_20200202_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='shipment_tracking_number',
        ),
        migrations.AddField(
            model_name='shipment',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
