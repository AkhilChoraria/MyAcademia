# Generated by Django 4.2.2 on 2023-06-17 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('credits', models.DecimalField(decimal_places=1, max_digits=3)),
                ('distrubution', models.CharField(choices=[('SCI', 'Science'), ('HUM', 'Humanities'), ('SSC', 'Social Science')], max_length=3)),
                ('prerequisites', models.JSONField()),
                ('exclusions', models.JSONField()),
            ],
        ),
    ]
