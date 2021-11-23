# Generated by Django 3.2.9 on 2021-11-23 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('distance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distancelocation',
            name='source_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.address'),
        ),
    ]
