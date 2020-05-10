from django.contrib import admin
from . import models

''' Made Inline group member model to admin so that we get the ability to modify them 
    and see the changes i.e. group members and could make changes'''
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)

