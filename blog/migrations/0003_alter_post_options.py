# Generated by Django 4.2.14 on 2024-07-25 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_content_post_created_on_post_excerpt_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
