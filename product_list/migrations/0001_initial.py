# Generated by Django 4.1.7 on 2023-05-29 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('intro', models.CharField(max_length=300)),
                ('info', models.TextField()),
                ('img_link', models.TextField()),
            ],
        ),
    ]
