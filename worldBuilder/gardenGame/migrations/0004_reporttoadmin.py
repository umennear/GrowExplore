# Generated by Django 4.0.3 on 2022-03-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gardenGame', '0003_rename_buidling_desc_buildingoftheday_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportToAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_name', models.CharField(max_length=200)),
                ('problem_description', models.CharField(max_length=200)),
            ],
        ),
    ]
