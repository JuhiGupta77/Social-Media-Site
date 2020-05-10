from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.db import IntegrityError
from django.views.generic import CreateView, DetailView, ListView, RedirectView
from groups.models import Group, GroupMember
from django.shortcuts import get_object_or_404
from . import models
''' was can make use of these built-in messages from django to display things '''
from django.contrib import messages

''' for creating a group '''
class CreateGroup(LoginRequiredMixin, CreateView):
    ''' fields need to get editted to '''
    fields = ('name', 'description')
    model = Group


''' for looking at a single group '''
class SingleGroup(DetailView):
    model = Group


''' for seeing the list of created groups '''
class ListGroups(ListView):
    model = Group


''' RedirectView helps to redirect to the url we want to '''
class JoinGroup(LoginRequiredMixin, RedirectView):

    ''' if you have joined the group then go back to that group's single joining page '''
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        ''' try and except are imp otherwise broken page will be displayed'''
        ''' it's because the user can make mistakes i.e. by being enrolled in a group and again trying to do so etc.'''
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Warning already a member !')
        else:
            messages.success(self.request, 'You are now a member!')

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, RedirectView):

    ''' if you have joined the group then go back to that group's single joining page '''
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug = self.kwargs.get('slug')
            ).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry you are not in this group !')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group !')

        return super().get(request, *args, **kwargs)

