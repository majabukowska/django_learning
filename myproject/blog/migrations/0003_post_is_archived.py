# Generated by Django 5.0.4 on 2024-04-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
    ]
