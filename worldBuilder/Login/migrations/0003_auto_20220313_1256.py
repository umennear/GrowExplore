# Generated by Django 3.0.8 on 2022-03-13 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20220313_1153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='db.sqlite3',
        ),
    ]
