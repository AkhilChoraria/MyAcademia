# Generated by Django 4.2.2 on 2023-06-19 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_rename_credits_course_credit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='prerequisites',
            new_name='pre_req',
        ),
    ]
