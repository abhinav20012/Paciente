# Generated by Django 4.1.3 on 2022-11-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_userinfo_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='document',
            field=models.FileField(null=True, upload_to='static/upload/<django.db.models.fields.EmailField>'),
        ),
    ]
