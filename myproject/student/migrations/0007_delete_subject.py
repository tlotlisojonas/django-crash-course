# Generated by Django 3.2.5 on 2021-07-23 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_subject_subject'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
