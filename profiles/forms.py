from django import forms
from django.contrib.auth.models import User
from .models import Profile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  
        fields = ['user', 'image', 'firstname', 'lastname', 'username']
        
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username
        
    def save(self, commit=True):
        profile = super(EditProfileForm, self).save(commit=False)
        new_image = self.cleaned_data.get('image')
        new_firstname = self.cleaned_data.get('firstname')
        new_lastname = self. cleaned_data.get('lastname')
        new_username = self.cleaned_data.get('username')
        
        # Update profile image
        if new_image:
            profile.image = new_image

        if new_firstname and new_firstname != profile.user.firstname:
            profile.user.firstname = new_firstname
            profile.user.save()
        
        if new_lastname and new_lastname != profile.user.lastname:
            profile.user.lastname = new_lastname
            profile.user.save() 

        if new_username and new_username != profile.user.username:
            profile.user.username = new_username
            profile.user.save() 

        # Save changes
        if commit:
            profile.save()
        return profile