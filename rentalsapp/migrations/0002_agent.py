# Generated by Django 4.2 on 2024-12-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
