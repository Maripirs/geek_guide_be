# Generated by Django 4.1.5 on 2023-02-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0007_content_direction_extendedcontent_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='hashid',
            field=models.CharField(choices=[('legend', 'legend'), ('round', 'round'), ('turn', 'turn')], max_length=20),
        ),
    ]