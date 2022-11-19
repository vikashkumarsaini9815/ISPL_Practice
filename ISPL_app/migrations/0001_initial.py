# Generated by Django 4.1.3 on 2022-11-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact', models.CharField(max_length=12, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('school_name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=255, null=True)),
                ('project_idea', models.TextField(blank=True, null=True)),
                ('project_discrapition', models.TextField(blank=True, null=True)),
                ('student', models.ManyToManyField(to='ISPL_app.student')),
            ],
        ),
    ]
