# Generated by Django 4.2.2 on 2023-07-02 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_student_info_course_ta_info_course"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student_info",
            name="course",
        ),
        migrations.RemoveField(
            model_name="ta_info",
            name="course",
        ),
        migrations.AddField(
            model_name="student_info",
            name="course",
            field=models.ManyToManyField(null=True, to="api.courses"),
        ),
        migrations.AddField(
            model_name="ta_info",
            name="course",
            field=models.ManyToManyField(null=True, to="api.courses"),
        ),
    ]