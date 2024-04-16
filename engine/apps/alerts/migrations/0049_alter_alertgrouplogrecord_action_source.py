# Generated by Django 4.2.10 on 2024-03-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0048_alertgroupexternalid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertgrouplogrecord',
            name='action_source',
            field=models.SmallIntegerField(default=None, null=True, verbose_name=[(0, 'Slack'), (1, 'Web'), (2, 'Phone'), (3, 'Telegram'), (4, 'API'), (5, 'Backsync')]),
        ),
    ]