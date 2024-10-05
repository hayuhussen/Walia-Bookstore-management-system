from django import forms
from Campany.models import *







class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = "__all__"
from django import forms
from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 5:
            raise ValidationError("Book quantity is less than 5. Please restock soon!")
        return quantity

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"


class EventPostForm(forms.ModelForm):
    class Meta:
        model = EventPost
        fields = "__all__"


class AudioBookSForm(forms.ModelForm):
    class Meta:
        model = AudioBookS
        fields = "__all__"

class Walia_Published_BookForm(forms.ModelForm):
    class Meta:
        model = Walia_Published_Book
        fields = "__all__"


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = BookCategory
        fields = "__all__"


class EventPostImageForm(forms.ModelForm):
    class Meta:
        model = EventPostImage
        fields = "__all__"


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"


# class CartForm(forms.viewForm):
#     class Meta:
#         view = Cart
#         fields = "__all__"


class ConsignmentAgreementForm(forms.ModelForm):
    class Meta:
        model = ConsignmentAgreement
        fields = "__all__"


class BookLanaguageForm(forms.ModelForm):
    class Meta:
        model = BookLanaguage
        fields = "__all__"


class Customer_InformationForm(forms.ModelForm):
    class Meta:
        model = Customer_Information
        fields = "__all__"


class EBookForm(forms.ModelForm):
    class Meta:
        model = EBook
        fields = "__all__"


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"
