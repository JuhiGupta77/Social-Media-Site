from django.db import models
from django.urls import reverse

''' slugify helps to remove _, alphs-numeric, spaces , - '''
''' slugify removes above characters and fill them with dashes '''
from django.utils.text import slugify

''' helps us with link-embedding i.e. provide links and mark-down texts '''
import misaka

''' get_user_model will help us return the model that is currently active in this project '''
from django.contrib.auth import get_user_model
''' it allows us to call things of the current user session '''
User = get_user_model()

''' helps us to use custom templates '''
from django import template
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.CharField(blank=True, default='', max_length=256)
    ''' used by the misaka '''
    description_html = models.CharField(max_length=256, editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    ''' GroupMembers are related to the Group class (above) by Foreign_Key called memberships '''
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    ''' all users that are related to the User and are part of the group '''
    user = models.ForeignKey(User, related_name='user_group', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        # define two fields “unique” as couple
        unique_together = ('group', 'user')



