# Generated by Django 4.1.5 on 2023-02-01 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geeks', '0005_alter_content_options_content_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='type',
            field=models.CharField(choices=[('Icon Legend', 'Icon Legend'), ('Round Order', 'Round Order'), ('Turn Order', 'Turn Order')], max_length=20),
        ),
    ]
