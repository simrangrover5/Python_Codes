# Generated by Django 2.1.3 on 2018-11-27 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hno', models.CharField(max_length=10)),
                ('street_addr', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=20)),
                ('pin_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50)),
                ('fees', models.FloatField(max_length=6)),
                ('due', models.FloatField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('ph_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateTimeField(null=True)),
                ('ph_no', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='roll_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='address',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
    ]
