''' returns currently user model that is active in the project '''
from django.contrib.auth import get_user_model

''' UserCreationForm built-in in authorization creation package '''
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):  # don't create the same class name as that of Mixin one

    class Meta:
        ''' taking advantage of django.contrib.auth's built-in fields '''
        fields = ('username', 'email', 'password1', 'password2')
        ''' uses current who is allowed to visit our website '''
        model = get_user_model()

        ''' done initialization to have the auth form available to user with all fields to signin '''
        ''' memorize this '''
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            ''' our own custom labels; not mandatory to use '''
            ''' Display Name and Email Address will be placeholders for respective fields below in actual form on website '''
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Address'

