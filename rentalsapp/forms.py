from django import forms
from rentalsapp.models import ImageModel

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','rent','title','area','beds','baths','garage',]