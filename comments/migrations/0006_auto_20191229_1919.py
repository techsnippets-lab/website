# Generated by Django 2.0.7 on 2019-12-29 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_auto_20191229_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]