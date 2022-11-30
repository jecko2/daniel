# Generated by Django 4.1.3 on 2022-11-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('TOP', 'Top Stories'), ('POPULAR', 'Popular'), ('MEDICAL', 'Medical')], default='TOP', max_length=20, verbose_name='Category'),
        ),
    ]