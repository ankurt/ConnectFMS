from django import forms
from django.forms import ModelForm
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Building, Location, Utility, Post, Status, Comment
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')

    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.username = self.cleaned_data['username'].lower()
        user.email = self.cleaned_data['email'].lower()
        user.first_name = self.cleaned_data['first_name'].capitalize()
        user.last_name = self.cleaned_data['last_name'].capitalize()

        if commit:
            user.save()
        return user

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'

    def clean_street(self):
        return self.cleaned_data['street'].title()

    def clean_city(self):
        return self.cleaned_data['city'].capitalize()


class LocationForm(forms.ModelForm):
    building = forms.ModelChoiceField(queryset = Building.objects.all())

    class Meta:
        model = Location
        fields = ('name', 'description', 'building')
        widgets = {
            'description' : forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    def clean_name(self):
        return self.cleaned_data['name'].title()


class UtilityForm(forms.ModelForm):
    class Meta:
        model = Utility
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].title()


class PostForm(forms.ModelForm):
    location = forms.ModelChoiceField(queryset = Location.objects.all())
    utility = forms.ModelChoiceField(queryset = Utility.objects.all())

    class Meta:
        model = Post
        fields = ('user', 'created_at', 'location', 'description', 'utility', 'image')
        exclude = ('created_at', 'user')
        widgets = {
            'description': forms.Textarea(),
            'user': forms.HiddenInput(),
        }


class StatusForm(forms.ModelForm):
    utility = forms.ModelChoiceField(queryset = Utility.objects.all())

    class Meta:
        model = Status
        fields = ('user', 'created_at', 'description', 'utility', 'image')
        exclude = ('created_at', 'user')
        widgets = {
            'description': forms.Textarea(),
            'user': forms.HiddenInput(),
        }