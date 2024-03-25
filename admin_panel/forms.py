from django import forms
from dashboard.models import *
from main.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category', 'tags']


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['title', 'img']