# Generated by Django 4.1.5 on 2023-01-31 02:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0004_remove_section_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='content',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=2000), default=['hi'], size=None),
            preserve_default=False,
        ),
    ]
