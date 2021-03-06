# Generated by Django 2.1.2 on 2018-12-25 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import media_module.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermediafileslinks',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_media_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='media_module.Chat'),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='professor',
            field=models.ForeignKey(limit_choices_to=media_module.models.get_only_professors_q, on_delete=django.db.models.deletion.CASCADE, related_name='professor_chats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='student',
            field=models.ForeignKey(limit_choices_to=media_module.models.get_only_students_q, on_delete=django.db.models.deletion.CASCADE, related_name='student_chats', to=settings.AUTH_USER_MODEL),
        ),
    ]
