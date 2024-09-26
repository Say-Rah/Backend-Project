from django.db import models
from groups.models import StudyGroup

# Create your models here.
class StudySession(models.Model):
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name="sessions")
    date = models.DateField()
    time = models.TimeField()
    topic = models.CharField(max_length=255)
    duration = models.CharField(choices=[('1 month', '1 month'),('2 months', '2 months'),('3 months', '3 months'), ], max_length= 50)  # Stores time duration

    def __str__(self):
        return f"{self.topic} on {self.date} at {self.time}"
    
        # return self.title
