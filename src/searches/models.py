from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Search(models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True)
    query     = models.CharField(max_length= 360)
    timestemp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
