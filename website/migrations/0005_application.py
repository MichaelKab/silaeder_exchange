# Generated by Django 3.1.4 on 2021-01-04 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20201228_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_zone', models.CharField(max_length=1000)),
                ('wont', models.CharField(max_length=1000)),
                ('know', models.CharField(max_length=1000)),
                ('contacts', models.CharField(max_length=1000)),
                ('user_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
