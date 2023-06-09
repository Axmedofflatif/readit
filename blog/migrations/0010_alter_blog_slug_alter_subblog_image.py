# Generated by Django 4.2.1 on 2023-06-12 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=221, null=True, unique_for_date='created_date'),
        ),
        migrations.AlterField(
            model_name='subblog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/'),
        ),
    ]
