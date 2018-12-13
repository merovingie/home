from django import forms
from .models import Entrynew, boxDisplayView
import re

# class Entryform(forms.Form):
#     message = forms.CharField(widget = forms.Textarea)
    


class Entrymodel(forms.ModelForm):

    class Meta:
        model = Entrynew
        fields = ('starting_DIDSTR',)

class Boxmodel(forms.ModelForm):

    class Meta:
        model = Entrynew
        fields = ('message_field',)

class BoxDisplayForm(forms.ModelForm):

    class Meta:
        model = boxDisplayView
        fields = ('cassettes','contianers','DID_type','DID_comments',)

    
