from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()


class GroupQuerySet(models.QuerySet):
    def search(self, query):
        lookup =(
            Q(posts__text__icontains=query)|
            Q(posts__user__username__icontains=query)|
            Q(name__icontains=query)|
            Q(slug__icontains=query)|
            Q(description__icontains=query)
        )
        return self.filter(lookup)

class GroupManager(models.Manager):

    def get_queryset(self):
        return GroupQuerySet(self.model, using=self._db)


    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class Group(models.Model):
    members = models.ManyToManyField(User, through='GroupMember')
    name = models.CharField(max_length =70, unique = True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = GroupManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']





class GroupMember(models.Model):
    user  = models.ForeignKey(User ,related_name='user_groups' ,on_delete=models.CASCADE)
    group = models.ForeignKey(Group ,related_name='memberships' ,on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username


    class Meta:
        unique_together = ('user', 'group')
