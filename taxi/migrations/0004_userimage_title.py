# Generated by Django 2.1.5 on 2019-08-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0003_auto_20190808_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='userimage',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]