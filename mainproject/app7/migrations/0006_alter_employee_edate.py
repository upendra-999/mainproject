# Generated by Django 4.1.3 on 2022-12-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app7', '0005_alter_employee_edate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='edate',
            field=models.CharField(max_length=50),
        ),
    ]
