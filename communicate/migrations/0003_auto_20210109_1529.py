# Generated by Django 3.1.4 on 2021-01-09 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communicate', '0002_auto_20210109_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_bgm_on',
            new_name='is_bgm_on',
        ),
    ]