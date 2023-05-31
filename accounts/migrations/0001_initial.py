# Generated by Django 4.2.1 on 2023-05-30 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("phone_number", models.CharField(blank=True, max_length=12)),
                (
                    "role",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[
                            (1, "Owner"),
                            (2, "Vendor"),
                            (3, "Agent"),
                            (4, "Subagent"),
                            (5, "Tenent"),
                            (6, "Associate"),
                        ],
                        null=True,
                    ),
                ),
                ("company", models.CharField(blank=True, max_length=100)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("last_login", models.DateTimeField(auto_now_add=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_superadmin", models.BooleanField(default=False)),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Contactus",
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
                ("fullname", models.CharField(blank=True, max_length=100, null=True)),
                ("mobileno", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                ("address", models.CharField(blank=True, max_length=100, null=True)),
                ("purpose", models.CharField(blank=True, max_length=200, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("last_login", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="CrudUser",
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
                ("name", models.CharField(blank=True, max_length=30)),
                ("address", models.CharField(blank=True, max_length=100)),
                ("age", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True, null=True, upload_to="users/profile_pictures"
                    ),
                ),
                (
                    "cover_photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="users/cover_photos"
                    ),
                ),
                ("address", models.CharField(blank=True, max_length=250, null=True)),
                ("country", models.CharField(blank=True, max_length=15, null=True)),
                ("state", models.CharField(blank=True, max_length=15, null=True)),
                ("city", models.CharField(blank=True, max_length=15, null=True)),
                ("pin_code", models.CharField(blank=True, max_length=6, null=True)),
                ("latitude", models.CharField(blank=True, max_length=20, null=True)),
                ("longitude", models.CharField(blank=True, max_length=20, null=True)),
                ("location", models.CharField(blank=True, max_length=20, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]