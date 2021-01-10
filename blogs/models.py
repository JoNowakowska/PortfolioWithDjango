from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    publication_datetime = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) > 100:
            return self.body[:99] + '...'

        return self.body

    def publication_date(self):
        return self.publication_datetime.strftime('%e %B %Y')