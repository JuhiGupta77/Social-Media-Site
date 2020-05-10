from django.db import models
from django.contrib import auth # taking advantage of Django's built-in authentication for users that way we dont have to make models for users


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        ''' auth.models.User has built-in username , pswd, etc. to automatically
            signin up website and django will take care of all that stuff '''
        return "@{}".format(self.username)
