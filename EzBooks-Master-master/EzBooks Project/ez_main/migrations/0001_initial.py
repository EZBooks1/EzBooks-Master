# Generated by Django 2.2.6 on 2019-11-13 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

   initial = True

   dependencies = 
   [
      ('users', '0006_remove_user_profile_is_staff'),
   ]

   operations = 
   [
      migrations.CreateModel
      (
         name   = 'Class_schedule',
         fields = 
         [
            ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ('class1', models.CharField(blank=True, max_length=200, null=True)),
            ('class2', models.CharField(blank=True, max_length=200, null=True)),
            ('class3', models.CharField(blank=True, max_length=200, null=True)),
            ('class4', models.CharField(blank=True, max_length=200, null=True)),
            ('class5', models.CharField(blank=True, max_length=200, null=True)),
            ('class6', models.CharField(blank=True, max_length=200, null=True)),
         ],
      ),
      migrations.CreateModel
      (
         name   = 'Classes_list',
         fields = 
         [
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('class_name', models.CharField(max_length=200)),
            ('major', models.CharField(max_length=100)),
            ('class_extension', models.CharField(max_length=200)),
            ('credit', models.IntegerField(default=25)),
         ],
      ),
   ]