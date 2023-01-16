# Generated by Django 3.2.14 on 2022-12-01 10:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acls', '0004_auto_20220831_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginacl',
            name='action',
            field=models.CharField(default='reject', max_length=64, verbose_name='Action'),
        ),
        migrations.AlterField(
            model_name='loginacl',
            name='reviewers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Reviewers'),
        ),
        migrations.AlterField(
            model_name='loginassetacl',
            name='action',
            field=models.CharField(default='reject', max_length=64, verbose_name='Action'),
        ),
        migrations.AlterField(
            model_name='loginassetacl',
            name='reviewers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Reviewers'),
        ),
    ]