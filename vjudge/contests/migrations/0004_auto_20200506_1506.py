# Generated by Django 3.0.4 on 2020-05-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_auto_20200506_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='clength',
            field=models.TextField(),
        ),
    ]
