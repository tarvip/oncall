# Generated by Django 4.2.6 on 2023-11-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_alertgroupassociatedlabel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertreceivechannelassociatedlabel',
            name='inheritable',
            field=models.BooleanField(default=True, null=True),
        ),
    ]