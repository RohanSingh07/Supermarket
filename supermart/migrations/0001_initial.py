# Generated by Django 3.2 on 2021-12-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(blank=True, choices=[('Household', 'Household'), ('food', 'food'), ('beverage', 'beverage')], max_length=50, null=True)),
                ('sub_category', models.CharField(blank=True, max_length=50, null=True)),
                ('amount', models.FloatField()),
            ],
        ),
    ]
