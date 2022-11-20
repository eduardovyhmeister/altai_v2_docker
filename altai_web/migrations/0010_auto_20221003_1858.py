# Generated by Django 3.2.15 on 2022-10-03 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('altai_web', '0009_auto_20220930_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='taiprm',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='altai_web.taiprm'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A1Q27',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A1Q28',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A1Q29',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A1Q31',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q12',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q13',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q14',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q16',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q17',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q18',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q19',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q20',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q21',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q22',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q23',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q26',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q27',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q28',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q29',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q30',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q33',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q34',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q35',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q36',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q37',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q38',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q39',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q40',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q41',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q7',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A2Q8',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A3Q1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A4Q10',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A4Q6',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q10',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q11',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q12',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q13',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q2',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q5',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q6',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q7',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q8',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='A7Q9',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ("Don't know", "Don't know")], default='Unspecified', max_length=100, null=True),
        ),
    ]
