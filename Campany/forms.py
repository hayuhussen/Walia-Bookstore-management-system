# from django import forms
# from .models import Contact


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ["name", "email", "message"]


from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        # self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Email'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Message', 'rows': 4})
