# Generated by Django 4.2.5 on 2023-09-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bbs", "0004_remove_picture_caption"),
    ]

    operations = [
        migrations.AlterField(
            model_name="picture",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="ads_pictures"),
        ),
    ]