# Generated by Django 4.0.6 on 2022-07-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('knows', models.CharField(max_length=20)),
                ('learning', models.CharField(max_length=20)),
            ],
        ),
    ]
