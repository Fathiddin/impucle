from django.forms import ModelForm, TextInput
from .models import Registration

# Add new book form


class AddPostForm(ModelForm):

    class Meta:
        model = Registration
        fields = ["name", "mail", "phone"]
        
        widgets = {
            "name": TextInput(attrs={"placeholder":"Ismingiz", "maxlength":"200"}),
            "mail": TextInput(attrs={"placeholder":"E-pochta", "maxlength":"200", "type":"mail"}),
            "phone": TextInput(attrs={"placeholder":"Telefon raqam", "maxlength":"50", "type":"number"}),
        }