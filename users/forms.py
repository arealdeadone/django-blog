from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, CounsellorDetails


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateFrom(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateFrom, self).__init__(*args, **kwargs)
        self.fields['is_counsellor'].label = 'Become a Counsellor'
        self.fields['image'].label = 'Upload a new Image'

    class Meta:
        model = Profile
        fields = ['bio', 'is_counsellor', 'image']


class CounsellorDetailsUpdateForm(forms.ModelForm):
    fee = forms.IntegerField()
    turn_around_time = forms.IntegerField()

    class Meta:
        model = CounsellorDetails
        fields = ['fee', 'turn_around_time']
