# Generated by Django 2.1.5 on 2019-08-08 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0004_userimage_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userimage',
            options={'verbose_name': 'photo', 'verbose_name_plural': 'photo'},
        ),
    ]
