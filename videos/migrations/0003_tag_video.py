# Generated by Django 3.2.12 on 2022-08-01 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20220801_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('view_count', models.PositiveBigIntegerField()),
                ('like_count', models.PositiveBigIntegerField()),
                ('favorite_count', models.PositiveBigIntegerField()),
                ('comment_count', models.PositiveBigIntegerField()),
                ('published_at', models.DateTimeField(blank=True)),
                ('duration', models.CharField(max_length=100)),
                ('performance_score', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.channel')),
                ('tags', models.ManyToManyField(to='videos.Tag')),
            ],
            options={
                'db_table': 'video',
            },
        ),
    ]
