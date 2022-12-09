# Generated by Django 4.1.4 on 2022-12-09 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Fav",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("song_title", models.CharField(max_length=100)),
                ("artist", models.CharField(max_length=100)),
                ("album", models.CharField(max_length=100)),
                ("year_of_release", models.DateField()),
                ("rating", models.IntegerField()),
                (
                    "reviewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Opinion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("opinion", models.TextField(max_length=500)),
                (
                    "reviewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "song",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="favsongsapp.fav",
                    ),
                ),
            ],
        ),
    ]
