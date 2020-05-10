from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

''' import django-braces module '''
from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin, ListView):
    model = models.Post
    ''' tuple related model i.e. the foreign keys for this post '''
    select_related = ('user', 'group')


class UserPosts(ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            ''' the user that belongs to this particular post '''
            ''' get the username exactly with the username whosever is logged-in '''
            self.post_user = User.objects.prefetch_related("posts").get(username__iexact=self.kwargs.get("username"))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, DetailView):
    ''' SelectRelatedMixin: A simple mixin which allows you to specify a list or tuple of foreign key fields to perform a select_related on. '''
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    fields = ('message', 'group')
    model = models.Post

    ''' connect form to the user itself '''
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")
    # template_name = 'posts/post_confirm_delete.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        ''' added message-test to message field '''
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)








