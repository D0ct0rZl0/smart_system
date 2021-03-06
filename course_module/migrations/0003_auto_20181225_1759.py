# Generated by Django 2.1.2 on 2018-12-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0002_auto_20181225_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='containertocourse',
            name='instant_accept',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='containertocourse',
            name='min_quantity',
            field=models.SmallIntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='containertocourse',
            name='quantity',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
