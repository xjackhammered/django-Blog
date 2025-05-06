from django.forms import ModelForm
from .models import Thoughts

class PostForm(ModelForm):
    class Meta:
        model = Thoughts
        fields = '__all__'
        exclude = ['host']