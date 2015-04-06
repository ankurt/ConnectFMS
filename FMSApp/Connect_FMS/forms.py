from django import forms
from django.forms import ModelForm
from django.forms import ModelChoiceField

from .models import User, Building, Location, Utility, Post, Status, Comment


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_andrewid(self):
        return self.cleaned_data['andrewid'].lower()

    def clean_first_name(self):
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].capitalize()

    def clean_email(self):
        return self.cleaned_data['email'].lower()


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
    user = forms.ModelChoiceField(queryset = User.objects.all())#, widget = forms.HiddenInput)
    location = forms.ModelChoiceField(queryset = Location.objects.all())
    utility = forms.ModelChoiceField(queryset = Utility.objects.all())

    class Meta:
        model = Post
        # get hidden id from current user - 
        # http://stackoverflow.com/questions/9269945/how-do-i-pass-the-current-user-id-as-a-hidden-field-in-a-django-form
        fields = ('user', 'created_at', 'location', 'description', 'utility', 'image')
        exclude = ('created_at',)
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }


class StatusForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset = User.objects.all(), widget = forms.HiddenInput())
    created_at = forms.DateTimeField(widget = forms.HiddenInput())
    utility = forms.ModelChoiceField(queryset = Utility.objects.all())

    class Meta:
        model = Status
        fields = ('user', 'created_at', 'description', 'utility', 'image')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('description')

#     def __init__(self, *args, **kwargs):
#         self.type_of_post_id = kwargs.pop('type_of_post_id')   # the post instance
#         super().__init__(*args, **kwargs)

#     def save(self):
#         comment = super().save(commit=False)
#         comment.type_of_post_id = self.type_of_post_id
#         comment.save()
#         return comment