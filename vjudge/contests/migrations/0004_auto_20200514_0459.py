# Generated by Django 3.0.4 on 2020-05-13 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_auto_20200514_0456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranklist',
            name='totalac',
        ),
        migrations.RemoveField(
            model_name='ranklist',
            name='totalpoint',
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb1',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb10',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb2',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb3',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb4',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb5',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb6',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb7',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb8',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='ranklist',
            name='tpb9',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=19),
        ),
    ]
