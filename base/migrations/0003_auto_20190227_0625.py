# Generated by Django 2.1.7 on 2019-02-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20190225_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='questions',
        ),
        migrations.AddField(
            model_name='question',
            name='themes',
            field=models.ManyToManyField(to='base.Theme'),
        ),
    ]
