from django.db import models


class Video(models.Model):
    caption = models.CharField(max_length=255, null=True)
    video = models.FileField(upload_to='videos/%y')
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.caption
