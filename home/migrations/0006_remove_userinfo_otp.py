# Generated by Django 4.1.3 on 2022-11-25 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_userinfo_delete_signupinfo1_delete_signupinfo2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='otp',
        ),
    ]