# Generated by Django 3.0.4 on 2021-03-09 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210309_1119'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]