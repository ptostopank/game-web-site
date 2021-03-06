# Generated by Django 3.1.5 on 2021-01-26 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('first_release_date', models.DateTimeField(verbose_name='first_release_date')),
                ('rating', models.FloatField(null=True, verbose_name='rating')),
                ('rating_count', models.IntegerField(null=True, verbose_name='rating_count')),
                ('aggregated_rating', models.FloatField(null=True, verbose_name='aggregated_rating')),
                ('aggregated_rating_count', models.IntegerField(null=True, verbose_name='aggregated_rating_count')),
                ('summary', models.TextField(verbose_name='summary')),
                ('cover', models.URLField(null=True, verbose_name='cover')),
            ],
        ),
        migrations.CreateModel(
            name='ScreenShots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Url')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_screenshots', to='main.game')),
            ],
        ),
        migrations.CreateModel(
            name='Platforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_platforms', to='main.game')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_genre', to='main.game')),
            ],
        ),
    ]
