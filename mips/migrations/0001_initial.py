# Generated by Django 2.2.2 on 2019-08-21 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson_number', models.IntegerField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LessonParagraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mips.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='LessonParagaphImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.CharField(max_length=150)),
                ('lesson_paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mips.LessonParagraph')),
            ],
        ),
        migrations.CreateModel(
            name='LessonNavigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anchorName', models.CharField(max_length=75)),
                ('anchorID', models.CharField(max_length=75)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mips.Lesson')),
            ],
        ),
    ]
