# Generated by Django 3.2.15 on 2022-10-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('altai_web', '0015_auto_20221018_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='taiprm',
            name='RPN',
            field=models.TextField(default='[]', null=True),
        ),
    ]
