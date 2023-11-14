from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=250)
    artist_name = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# class Collection(models.Model):
#     name = models.CharField(max_length=250)

#     def __str__(self):
#         return self.name