# Generated by Django 2.2.5 on 2020-06-15 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoccerApp', '0004_auto_20200613_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soccermatch',
            name='MatchDate',
            field=models.DateField(blank=True, verbose_name='Date(mm/dd/2020)'),
        ),
        migrations.AlterField(
            model_name='soccermatch',
            name='MatchTime',
            field=models.TimeField(),
        ),
    ]