# Generated by Django 5.0.2 on 2024-05-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('occupation', models.CharField(max_length=100)),
                ('past_attendance', models.BooleanField()),
                ('social_media_followers', models.IntegerField()),
                ('interest_in_music', models.BooleanField()),
                ('interest_in_art', models.BooleanField()),
                ('interest_in_technology', models.BooleanField()),
                ('distance_from_venue', models.FloatField()),
                ('has_plus_one', models.BooleanField()),
                ('invited', models.BooleanField(default=False)),
            ],
        ),
    ]