# Generated by Django 3.2.9 on 2021-11-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Architect_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Bio', models.TextField(max_length=100)),
                ('experience', models.CharField(max_length=50)),
            ],
        ),
    ]