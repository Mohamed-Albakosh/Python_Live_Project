# Generated by Django 2.2.5 on 2020-06-13 10:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('SoccerApp', '0002_auto_20200612_1237'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='referees',
            managers=[
                ('RefereesOB', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='soccermatch',
            managers=[
                ('SoccerMatchOB', django.db.models.manager.Manager()),
            ],
        ),
    ]