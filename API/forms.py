from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
    
    class Meta:
        model = Friend
        fields = '__all__'