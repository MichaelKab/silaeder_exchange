# Generated by Django 3.1.5 on 2021-03-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20210306_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='short_description',
            field=models.CharField(default='-', max_length=400),
        ),
    ]
