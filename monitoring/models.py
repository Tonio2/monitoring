from django.db import models
from django.contrib.auth.models import User

class FollowUp(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        activity = models.CharField(max_length=200)

        def __str__(self):
            return str(self.user) + ': ' + self.activity
