# Generated by Django 3.2.5 on 2021-07-23 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_delete_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('Eng', 'English'), ('Physics', 'Physical Sciences'), ('LS', 'Life Sciences'), ('LO', 'Life Orientation'), ('Maths', 'Mathematics')], default='English', max_length=200)),
                ('learner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.learner')),
            ],
        ),
    ]