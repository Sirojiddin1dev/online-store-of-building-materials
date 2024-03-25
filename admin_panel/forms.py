from django import forms
from dashboard.models import Products

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
