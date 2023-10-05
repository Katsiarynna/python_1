from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk} \n {self.name} \n {self.content} \n {self.is_private}'
