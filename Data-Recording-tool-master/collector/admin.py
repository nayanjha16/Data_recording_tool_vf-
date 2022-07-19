from django.contrib import admin
from . import models

admin.site.register(models.sentences)
admin.site.register(models.audio_files)
