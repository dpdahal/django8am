# Generated by Django 4.2 on 2023-04-20 02:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='page/%Y/%m/%d/')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='summary',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
