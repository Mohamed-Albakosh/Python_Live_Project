# Generated by Django 2.2.5 on 2020-06-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoccerApp', '0003_auto_20200612_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soccermatch',
            name='MatchDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='soccermatch',
            name='MatchTime',
            field=models.DateTimeField(),
        ),
    ]
