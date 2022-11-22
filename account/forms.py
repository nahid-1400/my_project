from django import forms
from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True
            self.fields['special_user'].disabled = True
            self.fields['is_author'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'special_user', 'is_author']


class UpdateUser(forms.ModelForm):
    email = forms.EmailField()
    def __init__(self):
        self.fields['new_password1'].help_text = ''
        super(UpdateUser, self).__init__()
    class Meta:
        model = User
        fields = ['username']



class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exits_username = User.objects.filter(username=username).exists()
        if exits_username:
            forms.ValidationError('نام کاربری وجود دارد')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exits_email = User.objects.filter(email=email).exists()
        if exits_email:
            forms.ValidationError('نام کاربری وجود دارد')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            forms.ValidationError('رمز های عبور مطابقت ندارند')
        return password
