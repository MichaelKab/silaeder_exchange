# Generated by Django 3.1.4 on 2020-12-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20201225_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_with_skill',
            name='skill_main',
        ),
        migrations.AddField(
            model_name='user_with_skill',
            name='skill_string',
            field=models.CharField(default='-', max_length=60),
            preserve_default=False,
        ),
    ]
