# Generated by Django 3.0.5 on 2020-05-16 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basicinfo',
            fields=[
                ('id', models.IntegerField(blank=True)),
                ('name', models.TextField(blank=True, primary_key=True, serialize=False, unique=True)),
                ('validity', models.TextField(blank=True, null=True)),
                ('blank_pages', models.TextField(blank=True, null=True)),
                ('vaccination', models.TextField(blank=True, null=True)),
                ('amount_entry', models.TextField(blank=True, null=True)),
                ('amount_exit', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'basicinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VisaInformation',
            fields=[
                ('id', models.IntegerField(blank=True)),
                ('name', models.TextField(blank=True, primary_key=True, serialize=False, unique=True)),
                ('study_visa', models.TextField(blank=True, null=True)),
                ('visit_visa', models.TextField(blank=True, null=True)),
                ('business_visa', models.TextField(blank=True, null=True)),
                ('employment_visa', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'visa_information',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('email', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('subjects', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CountryImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=200, unique=True)),
                ('Country_photo', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='newScholarship',
            fields=[
                ('username', models.TextField()),
                ('email', models.TextField()),
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='scholars_list',
            fields=[
                ('Country', models.TextField()),
                ('Name', models.TextField(primary_key=True, serialize=False, unique=True)),
                ('Description', models.TextField()),
                ('level', models.TextField()),
                ('last_date', models.DateField()),
                ('scholarship', models.TextField()),
                ('link', models.TextField()),
                ('status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tourism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=200, unique=True)),
                ('Description', models.CharField(max_length=5000)),
            ],
        ),
    ]
