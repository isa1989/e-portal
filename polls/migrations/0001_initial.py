# Generated by Django 2.1.5 on 2019-02-11 07:36

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_a', ckeditor.fields.RichTextField()),
                ('content_a', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Learn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_l', models.CharField(max_length=100)),
                ('content_l', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpha', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_s', models.CharField(max_length=100)),
                ('content_s', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default='', max_length=200)),
                ('word_exp', models.TextField()),
                ('letter', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='connect', to='polls.Letter')),
            ],
        ),
        migrations.CreateModel(
            name='Yuklemeler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(blank=True, upload_to='uploads/%Y/%m/%d/', verbose_name='PDF yuklemeler')),
                ('namefile', models.CharField(blank=True, max_length=400, verbose_name='Yuklenen file adi.')),
            ],
        ),
        migrations.AddField(
            model_name='statistics',
            name='upload',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Yuklemeler', verbose_name='PDF yuklemeler'),
        ),
    ]
