# Generated by Django 3.1.3 on 2020-11-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20201113_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Coordinator',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
