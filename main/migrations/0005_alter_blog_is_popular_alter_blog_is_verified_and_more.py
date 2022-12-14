# Generated by Django 4.1.3 on 2022-12-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_blog_is_popular'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='is_popular',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_verified',
            field=models.CharField(choices=[('pending', 'pending'), ('Verified', 'Verified')], max_length=10),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
