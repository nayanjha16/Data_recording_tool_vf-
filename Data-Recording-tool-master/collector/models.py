from django.db import models
from django.contrib.auth.models import User


class sentences(models.Model):
    sentence = models.CharField(max_length=5000)

    def __str__(self):
        return self.sentence[:10]


class audio_files(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    sentence = models.ForeignKey(sentences,
                                 on_delete=models.CASCADE)
    audio = models.FileField(upload_to="audio",
                             blank=False,
                             null=False)

    def __str__(self):
        return self.user.username
