# Generated by Django 3.0.4 on 2020-03-28 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_auto_20200328_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
