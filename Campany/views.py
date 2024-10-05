from django.shortcuts import render
from django.core.mail import send_mail

from django.contrib import messages

import pyttsx3
from django.http import JsonResponse


import tempfile
import os
from PyPDF2 import PdfReader  # Use PdfReader instead of PdfFileReader
from gtts import gTTS


import facebook
from telegram import Bot
from django.shortcuts import render, redirect
from .models import Post
from .models import EventPostImage
from .models import AudioBook
from .models import EBook
from .models import AudioBookS
from .models import *




from .forms import ContactForm
from .models import BookCategory


from .models import BankInfo



from django.core.paginator import Paginator



from django.db.models import Q

def home_page(request):
    email = list(Subscriber.objects.filter().values_list('email', flat=True))
    print(email)

    welcome_section_list = WelcomeSection.objects.all()
    welcome_list = welcome.objects.all()

    slide_list = Slide.objects.all()
    fact_list = Fact.objects.all()
    audiobooks = AudioBook.objects.all()
    audiobook = AudioBookS.objects.all()
    videos = Video.objects.all()
    Walia_Published_Books = Walia_Published_Book.objects.all()  # Define here

    paginator = Paginator(Walia_Published_Books, 8)  # Show 8 books per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    Category_Filter_list = CategoryFilter.objects.all()
    books_home_list = BookHome.objects.all()
    features_home_list = FeatureHome.objects.all()
    Meet_Staff_list = MeetStaff.objects.all()
    team_member_list = TeamMember.objects.all()
    Event_home_list = EventHome.objects.all()
    Event_homeimages_list = EventHomeImage.objects.all()
    books = Book.objects.all()
    EventImage = EventPostImage.objects.all()
    Category = BookCategory.objects.all()

    if request.method == "POST":
        email = request.POST.get("email")
        sub, _ = Subscriber.objects.get_or_create(email=email)

    data = {
        "books": books,
        "Category": Category,
        "videos": videos,
        "audiobooks": audiobooks,
        "audiobook": audiobook,
        "service_list": welcome_section_list,
        "slide_list": slide_list,
        "welcome_list": welcome_list,
        "Category_Filter_list": Category_Filter_list,
        "books_home_list": books_home_list,
        "features_home_list": features_home_list,
        "Meet_Staff_list": Meet_Staff_list,
        "team_member_list": team_member_list,
        "Event_home_list": Event_home_list,
        "Event_homeimages_list": Event_homeimages_list,
        "fact_list": fact_list,
        "EventImage": EventImage,
        "PDFDocument": PDFDocument,
        "Walia_Published_Books": page_obj,  # Pass the page_obj to the template
    }

    return render(request, "Campany/index.html", data)


def index2(request):
    return render(request, "Campany/index-2.html")


from django.shortcuts import render


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "We recieved your message, and we will responed as soon as possible!",
            )
            return redirect("contact")
    else:
        form = ContactForm()

    return render(request, "Campany/contact.html", {"form": form})


def booksmediadetailv1(request):
    return render(request, "Campany/books-media-detail-v1.html")


def booksmediadetailv2(request):
    return render(request, "Campany/books-media-detail-v2.html")


def booksmediagirdviewv1(request):
    return render(request, "Campany/books-media-gird-view-v1.html")




def booksmediagirdviewv2(request):
    if request.method == "POST":
        title = request.POST.get("keywords", "")
        discount_price = request.POST.get("discount_price", "")
        category = request.POST.get("category", "")
        language = request.POST.get("language", "")
        author = request.POST.get("author", "")
        publish_date = request.POST.get("publish_date", "")
        order_by = request.POST.get("orderby", "")

        # Initialize the query with all books
        books = Book.objects.all().order_by("-id")

        # Apply filters based on form inputs
        if title:
            books = books.filter(title__icontains=title).order_by("-id")
        if discount_price and discount_price != "Search the discount_price":
            books = books.filter(discount_price=discount_price).order_by("-id")
        if category and category != "All Categories":
         
            books = books.filter(category__name=category)
        if language:
             books = books.filter(language__name__icontains=language)
        if author:
             books = books.filter(author__name__icontains=author)
        if publish_date:
             books = books.filter(publish_date=publish_date)

        # Apply ordering
        if order_by == "Sort by Title":
            books = books.order_by("title")
        elif order_by == "Sort by popularity":
            books = books.order_by(
                "-number_sold"
            )  # Assuming popularity is based on the number of books sold
        elif order_by == "Sort by rating":
            books = books.order_by(
                "-rating"
            )  # Assuming there's a rating field in your Book model
        elif order_by == "Sort by newness":
            books = books.order_by("-publish_date")
        elif order_by == "Sort by price":
            books = books.order_by("price")
        elif order_by == "Sort by Author":
            books = books.order_by("author__name")
        elif order_by == "Publishing Date":
            books = books.order_by("-publish_date")

        # Paginate books after all filters and ordering are applied
        paginator = Paginator(books, 9)  # Show 10 books per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    else:
        books = Book.objects.all().order_by("-id")
        paginator = Paginator(books, 9)  # Show 9 books per page
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    books_banners = BooksPageBanner.objects.all().order_by("-id")
    category_list = BookCategory.objects.all().order_by("-id")
    Lanaguage_list = BookLanaguage.objects.all().order_by("-id")
    category_filters = CategoryFilter.objects.all().order_by("-id")
    authors = Author.objects.all().order_by("-id")

    # Get unique discount prices from books
    discount_prices = (
        Book.objects.values_list("discount_price", flat=True)
        .distinct()
        .order_by("discount_price")
    )

    data = {
        "books_banners": books_banners,
        "category_list": category_list,
        "Lanaguage_list": Lanaguage_list,
        "category_filters": category_filters,
        "authors": authors,
        "books": page_obj,
        "discount_prices": discount_prices,
    }

    return render(request, "Campany/books-media-gird-view-v2.html", data)




def booksmedialistview(request):
    return render(request, "Campany/books-media-list-view.html")


def homev2(request):

    return render(request, "Campany/home-v2.html")


def homev3(request):
    return render(request, "Campany/home-v3.html")


def services(request):
    services = Service.objects.all()
    company_infos = CompanyInfo.objects.all()

    data = {
        "services": services,
        "company_infos": company_infos,
    }
    return render(request, "Campany/services.html", data)


def newseventsdetail(request, id):
    event = Event.objects.get(id=id)
    Event_news_list = EventNews.objects.all()
    recents = Event.objects.all().order_by("-created")
    return render(
        request,
        "Campany/news-events-detail.html",
        {
            "event": event,
            "Event_news_list": Event_news_list,
            "recent_news_list": recents,
        },
    )











def newseventslistview(request):
    events = Event.objects.all().order_by("-created")
    paginator = Paginator(events, 10)  # Adjust the number based on your needs
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    data = {
        "events": page_obj,
        "Event_news_list": EventNews.objects.all(),  # Assuming this is for other content
        "recent_news_list": Event.objects.all().order_by("-created")[
            :5
        ],  # Adjust as needed
    }
    return render(request, "Campany/news-events-list-view.html", data)


def a404(request):
    return render(request, "Campany/404.html")




def blogdetail(request, id):
    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(post__id=blog.id, status=True).order_by('-date')

    return render(
        request,
        "Campany/blog-detail.html",
        {
            "blog": blog,
            "comments": comments,
        },
    )


def blog(request):
    blogs = Blog.objects.all()

    data = {
        "blogs": blogs,
    }

    return render(request, "Campany/blog.html", data)


from chapa import Chapa
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
import random
import string
from .models import Book, BankInfo


def generate_random_string(length):
    # Define the characters to use for the random string
    characters = string.ascii_letters + string.digits
    # Generate a random string
    random_string = "".join(random.choice(characters) for i in range(length))
    return random_string







from .models import Transaction

def cart(request):
    banks = BankInfo.objects.all()
    book = None

    if request.method == "GET":
        book_id = request.GET.get("id")
        if book_id:
            book = get_object_or_404(Book, pk=book_id)
        else:
            return render(
                request,
                "Campany/cart.html",
                context={"banks": banks, "error": "Book ID is missing."},
            )

    if request.method == "POST":
        # Retrieve the book ID from the POST data
        book_id = request.POST.get("id")
        if not book_id:
            return render(
                request,
                "Campany/cart.html",
                context={"banks": banks, "error": "Book ID is missing."},
            )

        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return render(
                request,
                "Campany/cart.html",
                context={"banks": banks, "error": "Book not found."},
            )

        # Retrieve the data from the request body
        print("Submitting payment")
        trx_key = generate_random_string(12)
        body = request.POST
        print("body", body)
        number_of_books = int(body["numberOfBooks"])
        amount = number_of_books * float(body["amount"])

        if book.quantity < number_of_books:
            return render(
                request,
                "Campany/cart.html",
                context={
                    "banks": banks,
                    "book": book,
                    "error": "Not enough stock available.",
                },
            )

        data = {
            "email": body["email"],
            "phone": body["phone"],
            "first_name": body["firstName"],
            "last_name": body["lastName"],
            "amount": amount,
            "tx_ref": trx_key,
            "callback_url": f"http://localhost:3000/stays/booking/{trx_key}/",
            "customization": {
                "title": "Pay now",
                "description": "Payment for your services",
            },
        }

        chapa = Chapa(settings.CHAPA_SECRET_KEY)
        response = chapa.initialize(**data)

        print("\nresponse", response)

        # After successful response, return to the Chapa checkout_url
        if response["status"] == "success":
            if book.quantity > 0:
                book.quantity -= 1
                book.save()
                # Record the transaction
                Transaction.objects.create(
                    book=book,
                    customer=request.user,
                    amount_paid=amount,
                    payment_method="chapa",
                )
            else:
                return render(
                    request,
                    "Campany/cart.html",
                    context={
                        "banks": banks,
                        "book": book,
                        "error": "Book out of stock",
                    },
                )
            return redirect(response["data"]["checkout_url"])
        else:
            return render(
                request,
                "Campany/cart.html",
                context={"banks": banks, "book": book, "error": response["message"]},
            )

    total_amount = book.price if book else 0
    context = {"banks": banks, "book": book, "total_amount": total_amount}
    return render(request, "Campany/cart.html", context=context)



from django.db.models import Sum, Count
from django.db.models.functions import TruncYear, TruncMonth, TruncWeek

def transactions(request):
    transactions_by_year = Transaction.objects.annotate(year=TruncYear('payment_date')).values('year').annotate(total=Sum('amount_paid'), count=Count('id')).order_by('year')
    transactions_by_month = Transaction.objects.annotate(month=TruncMonth('payment_date')).values('month').annotate(total=Sum('amount_paid'), count=Count('id')).order_by('month')
    transactions_by_week = Transaction.objects.annotate(week=TruncWeek('payment_date')).values('week').annotate(total=Sum('amount_paid'), count=Count('id')).order_by('week')

    context = {
        'transactions_by_year': transactions_by_year,
        'transactions_by_month': transactions_by_month,
        'transactions_by_week': transactions_by_week,
    }
    return render(request, "Campany/transaction.html", context)

def checkout(request):
    return render(request, "Campany/checkout.html")


def history(request):
    user_info = None
    if "q" in request.GET:
        user_info = Customer_Information.objects.filter(phone_Number=request.GET["q"])
        print("History --> ", user_info)
    context = {"user_info": user_info}
    return render(request, "Campany/history.html", context=context)


def signin(request):
    return render(request, "Campany/signin.html")


def gallery(request):
    EventImage = EventPostImage.objects.all().order_by("-id")

    data = {
        "EventImage": EventImage,
    }
    return render(request, "Campany/gallery.html", data)


def event(request):
    events = EventPost.objects.all()

    data = {
        "events": events,
    }

    return render(request, "Campany/event.html", data)


def audio(request):

    audiobooks = AudioBook.objects.all().order_by("-id")
    audiobook = AudioBookS.objects.all().order_by("-id")
    paginator = Paginator(audiobook, 9)  # Adjust the number based on your needs
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # If the request is a POST, get the search keyword
    if request.method == "POST":
        title = request.POST.get("keywords", "")
        if title:
            # Filter audiobooks by title if a keyword is provided
            audiobooks = audiobooks.filter(title__icontains=title)
    print("Request method:", request.method)
    print("Search keyword:", request.POST.get("keywords", ""))

    data = {
        "audiobooks": audiobooks,
        "audiobook": audiobook,
        "audiobook": page_obj,
    }

    return render(request, "Campany/audio.html", data)


def ebook(request):
    EBooks = EBook.objects.all().order_by("-id")
    TextBook = AudioTextBook.objects.all()

    paginator = Paginator(EBooks, 9)  # Adjust the number based on your needs
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.method == "POST" and request.FILES.get("pdf_file"):
        pdf_file = request.FILES["pdf_file"]

        # Create a temporary directory to store intermediate files
        temp_dir = tempfile.mkdtemp()
        pdf_path = os.path.join(temp_dir, "input.pdf")
        audio_path = os.path.join(temp_dir, "output.mp3")

        # Save the uploaded PDF file to the temporary directory
        with open(pdf_path, "wb") as f:
            for chunk in pdf_file.chunks():
                f.write(chunk)

        # Extract text from the PDF using PdfReader
        text = ""
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Convert the extracted text to audio
        tts = gTTS(text)
        tts.save(audio_path)

        # Serve the audio file for download
        with open(audio_path, "rb") as audio_file:
            response = HttpResponse(audio_file.read(), content_type="audio/mpeg")
            response["Content-Disposition"] = 'attachment; filename="output.mp3"'
            return response

    for ebook in page_obj:
        if not AudioTextBook.audio_file:
            engine = pyttsx3.init()
            audio_file_path = (
                f"audio/{AudioTextBook.title}.mp3"  # Use title for filename
            )
            engine.save_to_file(ebook.title, audio_file_path)
            engine.runAndWait()
            AudioTextBook.audio_file = audio_file_path
            AudioTextBook.save()

    data = {
        "EBooks": EBooks,
        "TextBook": TextBook,
        "EBooks": page_obj,
    }

    return render(request, "Campany/ebook.html", data)


def footer(request):
    footers = footer.objects.all()

    data = {
        "footers": footers,
    }

    return render(request, "Campany/footer.html", data)


def create_post(request):
    if request.method == "POST":
        # Gevet the post data from the form
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        location = request.POST.get("location")
        date = request.POST.get("date")
        time = request.POST.get("time")

        # Save the post to the event website's database
        post = Post.objects.create(
            title=title,
            description=description,
            image=image,
            location=location,
            date=date,
            time=time,
        )

        # Post on Facebook
        facebook_access_token = "YOUR_FACEBOOK_ACCESS_TOKEN"
        facebook_page_id = "YOUR_FACEBOOK_PAGE_ID"
        facebook_api = facebook.GraphAPI(access_token=facebook_access_token)
        facebook_api.put_object(
            facebook_page_id,
            "feed",
            message="New post on the event website: " + post.title,
        )

        # Post on Telegram
        telegram_bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
        telegram_channel_id = "YOUR_TELEGRAM_CHANNEL_ID"
        telegram_bot = Bot(token=telegram_bot_token)
        telegram_bot.send_message(
            chat_id=telegram_channel_id,
            text="New post on the event website: " + post.title,
        )

        # Redirect to the post details page
        return redirect("post_details", post_id=post.id)
    else:
        # Render the form to create a new post

        return render(request, "Campany/create_post.html")
