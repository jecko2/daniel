# Generated by Django 4.1.3 on 2022-11-27 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_post_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'get_latest_by': '-pub_date', 'ordering': ['-title', '-pub_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]