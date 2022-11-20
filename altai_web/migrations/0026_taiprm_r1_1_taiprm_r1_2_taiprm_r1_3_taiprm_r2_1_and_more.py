# Generated by Django 4.1.3 on 2022-11-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('altai_web', '0025_taiprm_t3q17_taiprm_t3q17_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='taiprm',
            name='R1_1',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R1_2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R1_3',
            field=models.IntegerField(default=1000, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R2_1',
            field=models.IntegerField(default=200, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R2_2',
            field=models.IntegerField(default=800, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R2_3',
            field=models.IntegerField(default=1000, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R3_1',
            field=models.IntegerField(default=400, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R3_2',
            field=models.IntegerField(default=1000, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R3_3',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R4_1',
            field=models.IntegerField(default=800, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R4_2',
            field=models.IntegerField(default=1000, null=True),
        ),
        migrations.AddField(
            model_name='taiprm',
            name='R4_3',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
