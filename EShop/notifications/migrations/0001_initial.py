# Generated by Django 2.2.4 on 2020-02-12 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_how', models.CharField(choices=[('one', 'SMS'), ('two', 'Viber'), ('three', 'Mail'), ('four', 'Telegram')], default='three', max_length=1)),
                ('notification_what', models.TextField(max_length=255)),
                ('notification_date', models.DateTimeField(verbose_name='date published')),
                ('notification_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
