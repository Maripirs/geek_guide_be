# Generated by Django 4.1.5 on 2023-02-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0006_alter_section_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='direction',
            field=models.CharField(choices=[('flex-row', 'flex-row'), ('flex-col', 'flex-col')], default='flex-row', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extendedcontent',
            name='direction',
            field=models.CharField(choices=[('flex-row', 'flex-row'), ('flex-col', 'flex-col')], default='flex-row', max_length=20),
            preserve_default=False,
        ),
    ]
