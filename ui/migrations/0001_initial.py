# Generated by Django 3.0.4 on 2020-03-28 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('state', models.CharField(blank=True, choices=[(1, 'I am Safe'), (2, 'I am Panicked!'), (3, 'I am Affected!!')], max_length=50, null=True)),
                ('division', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('world_result', models.CharField(blank=True, max_length=200, null=True)),
                ('bangladesh_result', models.CharField(blank=True, max_length=500, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
