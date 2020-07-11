# Generated by Django 3.0.6 on 2020-07-10 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(choices=[(' ', ' '), ('S1R', 'S1R'), ('S3R', 'S3R'), ('S5R', 'S5R'), ('S7R', 'S7R'), ('S1LA', 'S1LA'), ('S1LB', 'S1LB'), ('S3LA', 'S3LA'), ('S3LB', 'S3LB'), ('S5LA', 'S5LA'), ('S5LB', 'S5LB'), ('S7LA', 'S7LA'), ('S7LB', 'S7LB'), ('S1EA', 'S1EA'), ('S1EB', 'S1EB'), ('S3EA', 'S3EA'), ('S3EB', 'S3EB'), ('S5EA', 'S5EA'), ('S5EB', 'S5EB'), ('S7EA', 'S7EA'), ('S7EB', 'S7EB'), ('S1CA', 'S1CA'), ('S1CB', 'S1CB'), ('S3CA', 'S3CA'), ('S3CB', 'S3CB'), ('S5CA', 'S5CA'), ('S5CB', 'S5CB'), ('S7CA', 'S7CA'), ('S7CB', 'S7CB'), ('S1MA', 'S1MA'), ('S1MB', 'S1MB'), ('S3MA', 'S3MA'), ('S3MB', 'S3MB'), ('S5MA', 'S5MA'), ('S5MB', 'S5MB'), ('S7MA', 'S7MA'), ('S7MB', 'S7MB')], default=' ', max_length=4)),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('contact', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('n', 'Non Binary'), ('na', 'Prefer not to say')], max_length=2)),
                ('tshirt_size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3, verbose_name='T-Shirt Size')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('contact', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('n', 'Non Binary'), ('na', 'Prefer not to say')], max_length=2)),
                ('bio', models.TextField()),
                ('tshirt_size', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3, verbose_name='T-Shirt Size')),
                ('skills', models.TextField()),
                ('educational_institution', models.CharField(max_length=128)),
                ('field_of_study', models.CharField(blank=True, choices=[('cs', 'Computer Science'), ('ec', 'Electronics and Communication'), ('me', 'Mechanical Engineering'), ('ce', 'Civil Engineering'), ('ee', 'Electrical and Electronis Engineering'), ('it', 'Information Technology')], max_length=64, verbose_name='Field of Study')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
