# Generated by Django 2.1.2 on 2018-10-08 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='idUsu',
        ),
        migrations.AddField(
            model_name='likes',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likes',
            name='idPost',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='insta.Post'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='likes',
            name='usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='posteado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=500),
        ),
    ]
