# Generated by Django 4.1.3 on 2022-11-30 10:40

from django.db import migrations
import django_editorjs.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=django_editorjs.fields.EditorJsField(),
        ),
    ]
