# Generated by Django 4.0.2 on 2022-02-21 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_category_resource_card'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='category',
        ),
        migrations.RemoveField(
            model_name='card',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]