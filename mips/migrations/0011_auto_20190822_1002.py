# Generated by Django 2.2.2 on 2019-08-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mips', '0010_lessonnavigation_lessonparagraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='instruction_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
