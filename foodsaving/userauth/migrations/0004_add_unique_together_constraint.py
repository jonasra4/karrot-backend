# Generated by Django 2.0.2 on 2018-03-02 16:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userauth', '0003_auto_20180114_1224'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='verificationcode',
            unique_together={('user', 'type')},
        ),
    ]
