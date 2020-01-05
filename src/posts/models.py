from django.db import models
from django.contrib.auth import get_user_model
from groups.models import Group
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)

    def __Str__(self):
        return self.user.username

    class Meta:
        ordering = ['-created_at', ]
        unique_together = ['user', 'text']
