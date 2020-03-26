# Generated by Django 3.0.4 on 2020-03-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0003_auto_20200323_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('world_result', models.CharField(blank=True, max_length=150, null=True)),
                ('bangladesh_result', models.CharField(blank=True, max_length=300, null=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='position',
            name='state',
            field=models.CharField(blank=True, choices=[(1, 'I am Safe'), (2, 'I am Panicked!'), (3, 'I am Affected!!')], max_length=50, null=True),
        ),
    ]
