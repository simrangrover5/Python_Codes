# Generated by Django 2.1.3 on 2018-11-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20181127_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='1234567890', max_length=15),
        ),
    ]
