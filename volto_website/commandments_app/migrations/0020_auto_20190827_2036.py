# Generated by Django 2.2.3 on 2019-08-27 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commandments_app', '0019_auto_20190826_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarybiblereference',
            name='commandment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='commandments_app.Commandment'),
        ),
    ]