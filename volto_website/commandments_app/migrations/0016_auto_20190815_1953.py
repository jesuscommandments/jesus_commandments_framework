# Generated by Django 2.2.4 on 2019-08-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commandments_app', '0015_tertiarybiblereference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='primarybiblereference',
            old_name='chapter',
            new_name='begin_chapter',
        ),
        migrations.RenameField(
            model_name='primarybiblereference',
            old_name='verse',
            new_name='begin_verse',
        ),
        migrations.RenameField(
            model_name='secondarybiblereference',
            old_name='chapter',
            new_name='begin_chapter',
        ),
        migrations.RenameField(
            model_name='secondarybiblereference',
            old_name='verse',
            new_name='begin_verse',
        ),
        migrations.RenameField(
            model_name='tertiarybiblereference',
            old_name='chapter',
            new_name='begin_chapter',
        ),
        migrations.RenameField(
            model_name='tertiarybiblereference',
            old_name='verse',
            new_name='begin_verse',
        ),
        migrations.AddField(
            model_name='primarybiblereference',
            name='end_chapter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='primarybiblereference',
            name='end_verse',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='secondarybiblereference',
            name='end_chapter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='secondarybiblereference',
            name='end_verse',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tertiarybiblereference',
            name='end_chapter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tertiarybiblereference',
            name='end_verse',
            field=models.IntegerField(default=0),
        ),
    ]