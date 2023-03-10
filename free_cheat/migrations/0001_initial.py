# Generated by Django 4.1.5 on 2023-01-13 07:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreePubgCheat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('about', ckeditor.fields.RichTextField()),
                ('cheat', models.FileField(upload_to='free-cheats/cheats/')),
                ('image', models.ImageField(upload_to='free-cheats/images/')),
                ('video', models.FileField(upload_to='free-cheats/videos/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
