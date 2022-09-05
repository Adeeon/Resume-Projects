# Generated by Django 4.0.6 on 2022-07-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('cohort', models.CharField(max_length=25)),
                ('favorite_topic', models.CharField(max_length=25)),
                ('favorite_teacher', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['-last_name'],
            },
        ),
    ]