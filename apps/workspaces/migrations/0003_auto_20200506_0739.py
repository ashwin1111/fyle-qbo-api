# Generated by Django 3.0.3 on 2020-05-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0002_workspacegeneralsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='fyle_org_id',
            field=models.CharField(help_text='org id', max_length=255, unique=True),
        ),
    ]
