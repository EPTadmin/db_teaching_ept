# Generated by Django 4.2.6 on 2023-11-13 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_teaching", "0006_alter_course_studiepoeng"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personcourse",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="personcourse_person",
                to="app_teaching.course",
            ),
        ),
        migrations.AlterField(
            model_name="personcourse",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="personcourse_person",
                to="app_teaching.person",
            ),
        ),
    ]
