from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class StudyGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_groups')
    members = models.ManyToManyField(User, related_name='study_groups')

    def __str__(self):
        return self.name