# Generated by Django 3.2.6 on 2021-11-22 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='imagem',
            field=models.ImageField(default=1, upload_to='produtos'),
            preserve_default=False,
        ),
    ]