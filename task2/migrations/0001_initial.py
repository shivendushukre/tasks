# Generated by Django 3.1 on 2020-08-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=15)),
                ('phone_no', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
