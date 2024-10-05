from django.db import models
from tinymce import models as tinymce_models
from phonenumber_field.modelfields import PhoneNumberField

import phonenumbers
from datetime import date
from django.core.exceptions import ValidationError


# from autoslug import AutoSlugField

from django.utils.translation import gettext_lazy as _


# Create your models here.


class Subscriber(models.Model):
    """Used to store subscribers"""

    email = models.EmailField()
   



class Slide(models.Model):
    image = models.ImageField(upload_to="slides/")
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    paragraph = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return self.title


class welcome(models.Model):
    image = models.ImageField(upload_to="welcome/")
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    paragraph = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return self.title


class Slide(models.Model):
    image = models.ImageField(upload_to="slides/")
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    paragraph = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Fact(models.Model):
    ICON_CHOICES = [
        ("ebook", "Ebook"),
        ("eaudio", "Eaudio"),
        ("magazine", "Magazine"),
        ("video", "Video"),
    ]

    icon = models.CharField(max_length=20, choices=ICON_CHOICES)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="fact/")
    counter = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "Facts"

    def __str__(self):
        return self.name


class WelcomeSection(models.Model):
    name = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return self.name


class CategoryFilter(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return self.title


class BookHome(models.Model):
    image = models.ImageField()
    Autor = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    price = models.FloatField()

    def __str__(self) -> str:
        return self.description


class FeatureHome(models.Model):
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    # classimage = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.description


class MeetStaff(models.Model):
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return self.description


class TeamMember(models.Model):
    image = models.ImageField(upload_to="teams/")
    name_member = models.CharField(max_length=200)
    span = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return self.description


class BooksPageBanner(models.Model):
    title = models.CharField(max_length=200)
    span = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    list1 = models.CharField(max_length=50)


class EventHome(models.Model):
    title = models.CharField(max_length=200)
    span = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return self.description


class EventHomeImage(models.Model):
    title = models.CharField(max_length=200)
    span = models.CharField(max_length=200)
    time = models.TimeField()
    lacation = models.CharField(max_length=50)
    date = models.DateTimeField(
        auto_now=True,
    )
    description = tinymce_models.HTMLField()
    image = models.ImageField(upload_to="event-images/")

    def __str__(self) -> str:
        return self.description


class ImageCategory(models.Model):
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.image.name


class EventNews(models.Model):
    image = models.ForeignKey(ImageCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    time = models.TimeField()
    lacation = models.CharField(max_length=50)
    date = models.DateTimeField(
        auto_now=True,
    )
    description = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return self.title


class Event(models.Model):
    image = models.ImageField(upload_to="events/")
    title = models.CharField(max_length=200)
    time = models.TimeField()
    location = models.CharField(max_length=50)
    date = models.DateTimeField(
        auto_now=True,
    )
    description = tinymce_models.HTMLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description


class EventPostImage(models.Model):
    image = models.ImageField(upload_to="post/")
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    image = models.ImageField(upload_to="blogs/")
    title = models.CharField(max_length=200)
    days = models.IntegerField(_("Number of days"))
    created = models.DateTimeField(auto_now_add=True)
    month = models.CharField(max_length=50)
    description = tinymce_models.HTMLField(max_length=9000)

    def __str__(self) -> str:
        return f"{self.title}"

    def comment_count(self):
        return Comment.objects.filter(post__id=self.pk).count()


class Comment(models.Model):
    name = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField()
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EventPost(models.Model):
    image = models.ImageField(upload_to="eventpost/")
    title = models.CharField(max_length=200)
    days = models.IntegerField(_("Number of days"))
    created = models.DateTimeField(auto_now_add=True)
    month = models.CharField(max_length=50)
    description = tinymce_models.HTMLField()

    def __str__(self) -> str:
        return f"{self.title}"


class Post(models.Model):
    """Stores entities of different posts"""

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="post_images")
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Address(models.Model):
    title = models.CharField(max_length=200)
    street = models.CharField(max_length=50)
    fax = PhoneNumberField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"


class Phone(models.Model):
    title = models.CharField(max_length=200)
    phone1 = PhoneNumberField()
    phone2 = PhoneNumberField()

    def __str__(self) -> str:
        return self.phone1


class Email(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BookLanaguage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    category = models.ForeignKey("BookCategory", on_delete=models.CASCADE)
    language = models.ForeignKey(
        "BookLanaguage", on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    quantity = models.IntegerField(default=1)
    description = tinymce_models.HTMLField()
    publish_date = models.DateField()
    image = models.ImageField(upload_to="books/", blank=True, null=True)

    
    number_sold = models.IntegerField(default=0)

    def clean(self):
        # Ensure publish_date is not in the future
        if self.publish_date > date.today():
            raise ValidationError("Publish date cannot be in the future.")

        # Ensure price is not negative
        if self.price < 0:
            raise ValidationError("Price cannot be negative.")

        # Ensure discount_price is not negative
        if self.discount_price is not None and self.discount_price < 0:
            raise ValidationError("Discount price cannot be negative.")

        # Ensure quantity is not negative
        if self.quantity < 0:
            raise ValidationError("Quantity cannot be negative.")

    def save(self, *args, **kwargs):
        # Call the clean method to run validations
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Customer_Information(models.Model):

    First_name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_Number = models.CharField(max_length=15)
    number_of_books = models.IntegerField()
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.phone_Number


class Walia_Published_Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    language = models.ForeignKey(
        "BookLanaguage", on_delete=models.CASCADE, null=True, blank=True
    )

    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    quantity = models.IntegerField(default=1)
    # audio_book = models.FileField(upload_to='audio_books', null=True, blank=True)
    description = tinymce_models.HTMLField()
    publish_date = models.DateField()
    image = models.ImageField(upload_to="books/", blank=True, null=True)
    number_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class ConsignmentAgreement(models.Model):
    consign_date = models.DateTimeField(auto_now=True)
    delivered_to = models.CharField(max_length=255)
    delivered_by = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(upload_to="ConsignmentAgreements/", blank=True, null=True)
    book_title = models.CharField(max_length=255)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    language = models.ForeignKey(
        "BookLanaguage", on_delete=models.CASCADE, null=True, blank=True
    )

    quantity = models.IntegerField()
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    national_id = models.ImageField(upload_to="national_id/", blank=True, null=True)
    consignee_signature = models.CharField(max_length=255)
    consigner_signature = models.CharField(max_length=255)
    contractual_obligation = models.TextField()
    nda_request_effective = models.BooleanField(default=False)
    copyright_infringement_claim = models.BooleanField(default=False)

    def clean(self):
        if self.quantity < 0:
            raise ValidationError("Quantity cannot be negative.")
        if self.retail_price < 0:
            raise ValidationError("Retail price cannot be negative.")
        if self.discount_percent < 0:
            raise ValidationError("Discount percent cannot be negative.")
        if self.total_price < 0:
            raise ValidationError("Total price cannot be negative.")

    def save(self, *args, **kwargs):
        self.clean()
        self.total_price = self.quantity * self.retail_price
        if self.discount_percent:
            discount_amount = self.total_price * (self.discount_percent / 100)
            self.total_price -= discount_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_title

        pass


from django.utils import timezone
from django.conf import settings

class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(default=timezone.now)
    payment_method = models.CharField(max_length=50, )

    def __str__(self):
        return f"{self.book.title} - {self.customer.username} - {self.payment_date}"

class Cart(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    is_edit_hold = models.BooleanField(default=False)
    is_cancel_hold = models.BooleanField(default=False)
    is_add_hold = models.BooleanField(default=False)
    is_remove = models.BooleanField(default=False)

    def __str__(self):
        return self.book.title

    

class PDFDocument(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pdf/", blank=True, null=True)
    pdf = models.FileField(upload_to="pdfs/")

    def __str__(self):
        return self.book.title


class AudioBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="Audio/", blank=True, null=True)
    audio_file = models.FileField(upload_to="audiobooks/")

    def __str__(self):
        return f"{self.book.title}"


class EBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="ebook/", blank=True, null=True)
    file = models.FileField(upload_to="ebooks/")

    def __str__(self):
        return f"{self.book.title}"


class AudioTextBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="ebook/", blank=True, null=True)
    file = models.FileField(upload_to="ebooks/")
    audio_file = models.FileField(
        upload_to="audio/", blank=True, null=True
    )  # New field for audio

    def __str__(self):
        return f"{self.title}"


class AudioBookS(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to="Audio/", blank=True, null=True)
    audio_file = models.FileField(upload_to="audiobooks/")
    background_color = models.CharField(max_length=7, default="#000000")

    def __str__(self):
        return f"{self.book.title}"


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.title


class footer(models.Model):
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField()
    address = models.TextField()
    phone = PhoneNumberField()
    email = models.EmailField()

    def __str__(self):
        return self.title


class BankInfo(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=25)
    account_name = models.CharField(max_length=50)

    def __str__(self):
        return self.bank_name


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to="service_icons/")

    def __str__(self):
        return self.title



class CompanyInfo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="company_images/")

    def __str__(self):
        return self.title
