# Generated by Django 5.1.4 on 2024-12-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_alter_course_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="description",
            field=models.TextField(verbose_name="description"),
        ),
    ]