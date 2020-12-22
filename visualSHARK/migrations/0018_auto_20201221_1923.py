# Generated by Django 2.2.13 on 2020-12-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualSHARK', '0017_technologylabelcommit_has_technology'),
    ]

    operations = [
        migrations.AddField(
            model_name='technologylabel',
            name='ident',
            field=models.CharField(default='t', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='technologylabel',
            name='times_used',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
