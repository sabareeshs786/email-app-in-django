# Generated by Django 4.0.3 on 2022-04-07 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_bindetails_id_inboxdetails_id_junkdetails_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bindetails',
            name='uid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='inboxdetails',
            name='uid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='junkdetails',
            name='uid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sentdetails',
            name='uid',
            field=models.CharField(max_length=100),
        ),
    ]