# Generated by Django 4.0.3 on 2022-04-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='image',
            field=models.ImageField(default='default-image.png', upload_to='recipe_images'),
        ),
    ]
