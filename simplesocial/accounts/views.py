''' reverse_lazy is used for signing-in and out '''
from django.urls import reverse_lazy

from . import forms
from django.views.generic import CreateView


class SignUp(CreateView):
    form_class = forms.UserCreateForm  # instantiated the form class we created in forms.py file
    success_url = reverse_lazy('login')  # go to login on form's successful submission
    template_name = 'accounts/signup.html'
