# Generated by Django 4.1.3 on 2022-11-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_signupinfo2_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupinfo2',
            name='document',
            field=models.FileField(null=True, upload_to=None),
        ),
    ]