# Generated by Django 4.0.4 on 2022-05-26 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=255)),
                ('last_name', models.CharField(db_index=True, max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
