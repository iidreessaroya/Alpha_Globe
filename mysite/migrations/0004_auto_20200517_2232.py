# Generated by Django 3.0.5 on 2020-05-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20200517_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='subjects',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]
