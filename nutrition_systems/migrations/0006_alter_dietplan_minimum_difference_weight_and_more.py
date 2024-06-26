# Generated by Django 4.2.7 on 2024-04-30 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_systems', '0005_dietplan_maximum_difference_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietplan',
            name='minimum_difference_weight',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
