# Generated by Django 3.0.7 on 2020-07-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
