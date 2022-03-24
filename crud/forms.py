from django.forms import ModelForm
from .models import Contact

class stockmarketForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    