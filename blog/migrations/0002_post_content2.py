# Generated by Django 2.1.5 on 2019-02-15 07:51

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content2',
            field=markdownx.models.MarkdownxField(default='This is content'),
            preserve_default=False,
        ),
    ]
