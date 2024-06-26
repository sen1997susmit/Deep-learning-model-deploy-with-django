# Generated by Django 3.0.3 on 2020-05-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('path', models.FilePathField(default='C:\\Users\\Marco\\PycharmProjects\\Deep-learning-model-deploy-with-django\\media', path='C:\\Users\\Marco\\PycharmProjects\\Deep-learning-model-deploy-with-django\\media')),
            ],
            options={
                'unique_together': {('file', 'path')},
            },
        ),
    ]
