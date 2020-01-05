from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.urls import reverse

GENDER_CHOICES = (
('male', 'male'),
('female', 'female'),
("other", "other")
)

class Profile(models.Model):
    PROUser = models.OneToOneField(User, on_delete=models.CASCADE)
    PROSlug = models.SlugField(blank= True, null = True)
    PROImg = models.ImageField(upload_to='profile/', blank= True, null = True)
    PROGender = models.CharField(max_length=6 ,choices=GENDER_CHOICES)
    PROCountry = CountryField()
    PROAddress = models.CharField(max_length = 100)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'


    def __str__(self):
        return '@{}'.format(self.PROUser.username)


    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={"slug":self.PROSlug})


    def save(self, *args, **kwargs):
        if not self.PROSlug:
            self.PROSlug = slugify(self.PROUser.username)
        super(Profile, self).save(*args, **kwargs)



def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(PROUser=kwargs['instance'])


post_save.connect(create_profile, sender=User)
