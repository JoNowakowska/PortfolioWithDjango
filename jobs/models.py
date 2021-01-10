from django.db import models


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        if len(self.summary) > 50:
            return self.summary[:49] + '...'

        return self.summary
