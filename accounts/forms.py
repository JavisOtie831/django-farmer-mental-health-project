from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "is_staff", "is_active")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'afya-input'})

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "is_staff", "is_active")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the default password hash field from edit view
        if 'password' in self.fields:
            del self.fields['password']
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'afya-input'})