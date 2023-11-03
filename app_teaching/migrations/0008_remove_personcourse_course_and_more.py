# Generated by Django 4.2.6 on 2023-11-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_teaching", "0007_rename_persontocourse_personcourse"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personcourse",
            name="course",
        ),
        migrations.RemoveField(
            model_name="personcourse",
            name="person",
        ),
        migrations.AddField(
            model_name="personcourse",
            name="course",
            field=models.ManyToManyField(
                related_name="course_amount", to="app_teaching.course"
            ),
        ),
        migrations.AddField(
            model_name="personcourse",
            name="person",
            field=models.ManyToManyField(
                related_name="person_amount", to="app_teaching.person"
            ),
        ),
    ]
