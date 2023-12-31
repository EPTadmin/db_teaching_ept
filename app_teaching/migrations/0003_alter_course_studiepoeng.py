# Generated by Django 4.2.6 on 2023-11-08 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_teaching", "0002_course_person_personcourse_delete_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="studiepoeng",
            field=models.FloatField(
                choices=[
                    ("3,75", "3,75"),
                    ("7,5", "7,5"),
                    ("10,0", "10"),
                    ("15,0", "15"),
                    ("20,0", "20"),
                    ("30,0", "30"),
                ],
                max_length=4,
            ),
        ),
    ]
