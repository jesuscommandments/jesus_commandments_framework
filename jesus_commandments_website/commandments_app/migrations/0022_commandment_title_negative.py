# Generated by Django 2.2.5 on 2019-09-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandments_app', '0021_auto_20190912_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='commandment',
            name='title_negative',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
