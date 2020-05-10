from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

from groups.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    ''' this field will be automatically be completed at the time it is posted by the user '''
    ''' at the time of posted it will pick up that date and time field, no need to fill it up manually '''
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        ''' every message is uniquely linked together to user'''
        unique_together = ['user', 'message']


