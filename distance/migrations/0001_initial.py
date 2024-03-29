# Generated by Django 3.2.9 on 2021-11-22 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistanceLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance_km', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('source_address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='location.address')),
            ],
        ),
    ]
