# Generated by Django 4.2.15 on 2024-11-26 13:37

import common.migrations.remove_field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0005_labelkeycache_prescribed_labelvaluecache_prescribed'),
    ]

    operations = [
        common.migrations.remove_field.RemoveFieldState(
            model_name='AlertReceiveChannelAssociatedLabel',
            name='inheritable',
        ),
    ]