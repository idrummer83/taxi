# Generated by Django 2.1.5 on 2019-08-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_auto_20190808_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/user/'),
        ),
    ]
