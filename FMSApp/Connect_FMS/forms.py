from django import forms
from django.forms import ModelForm
from django.forms import ModelChoiceField

from .models import User, Building, Location, Utility, Post, Status, Comment


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = '__all__'

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
            'building': forms.ModelChoiceField(queryset = Building.objects.all())
        }

class UtilityForm(ModelForm):
    class Meta:
        model = Utility
        fields = '__all__'

class PostForm(forms.Form):
    class Meta:
        model = Post
        exlude('votes', 'created_at', 'user')
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
            'location': forms.ModelChoiceField(queryset = Location.objects.all())
            'utility': forms.ModelChoiceField(queryset = Utility.objects.all())
        }

class StatusForm(forms.Form):
    class Meta:
        model = Status
        exlude('likes', 'created_at', 'user')
        location = forms.ModelChoiceField(queryset = Location.objects.all())
        utility = forms.ModelChoiceField(queryset = Utility.objects.all())
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
            'location': forms.ModelChoiceField(queryset = Location.objects.all())
            'utility': forms.ModelChoiceField(queryset = Utility.objects.all())
        }

class CommentForm(forms.Form):
    class Meta:
        model = Status
        exlude('created_at', 'user')