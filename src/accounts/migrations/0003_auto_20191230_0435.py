# Generated by Django 3.0.1 on 2019-12-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191229_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='PROImg',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
