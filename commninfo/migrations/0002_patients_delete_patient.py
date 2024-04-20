# Generated by Django 4.2.7 on 2023-11-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commninfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='patients',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('FirstName', models.CharField(blank=True, max_length=100)),
                ('LastName', models.CharField(blank=True, max_length=100)),
                ('Email', models.TextField(blank=True, max_length=100)),
                ('password', models.IntegerField(blank=True)),
                ('confpassword', models.IntegerField(blank=True)),
                ('dateofbirth', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='patient',
        ),
    ]
