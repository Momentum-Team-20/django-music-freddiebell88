from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=250)
    artist_name = models.CharField(max_length=250)
    created_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
