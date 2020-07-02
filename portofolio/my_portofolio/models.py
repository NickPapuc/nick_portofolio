from django.db import models

class Jobs(models.Model):
    # an image for the job
    images = models.ImageField(upload_to = 'images/')
    # a summary for the job
    summary = models.CharField(max_length = 200)

    def __str__(self):
        return self.summary
