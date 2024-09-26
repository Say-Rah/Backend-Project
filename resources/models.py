from django.db import models

# Create your models here.
class Resource(models.Model):
    group = models.ForeignKey('groups.StudyGroup', on_delete=models.CASCADE)  # Each resource belongs to a group
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='static/media', blank=True)
    pdf = models.FileField(upload_to='static/pdf', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
