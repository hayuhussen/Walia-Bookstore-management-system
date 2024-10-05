from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Campany.models import *
from .forms import *












@login_required
def dashboard(request):
    # Aggregate transaction data
    transactions_by_year = Transaction.objects.annotate(year=TruncYear('payment_date')).values('year').annotate(total=Sum('amount_paid')).order_by('year')
    transactions_by_month = Transaction.objects.annotate(month=TruncMonth('payment_date')).values('month').annotate(total=Sum('amount_paid')).order_by('month')
    transactions_by_week = Transaction.objects.annotate(week=TruncWeek('payment_date')).values('week').annotate(total=Sum('amount_paid')).order_by('week')
    
    # Total counts for books, audiobooks, and ebooks
    total_books = Book.objects.count()
    total_audiobooks = AudioBookS.objects.count()
    total_ebooks = EBook.objects.count()

    return render(request, "customadmin/dashboard.html", {
        'transactions_by_year': transactions_by_year,
        'transactions_by_month': transactions_by_month,
        'transactions_by_week': transactions_by_week,
        'total_books': total_books,
        'total_audiobooks': total_audiobooks,
        'total_ebooks': total_ebooks,
    })









# ========================== EVENT VIEWS ==========================


@login_required
def events(request):
    count = Event.objects.count()
    return render(
        request,
        "customadmin/events/events.html",
        {
            "count": count,
            "events": Event.objects.all(),
        },
    )


@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():

            obj = form.save(commit=False)
            obj.save()
            message = f'title: {obj.title} \nDescription: {obj.description} \nmonth: {obj.month} \ncreated: {obj.created} '
            email = list(Subscriber.objects.filter().values_list('email', flat=True))
            send_mail(
            subject="Thank you for subscribing to our newsletter!",
            message=message,
            from_email="hayuya617@gmail.com",
            recipient_list=email,
        )




            
            messages.success(request, "New event created succussfully.")
            return redirect("events")
    else:
        form = EventForm()

    return render(request, "customadmin/events/event_form.html", {"form": form})


@login_required
def event_update(request, id):
    event = Event.objects.get(id=id)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated succussfully.")
            return redirect("events")
    else:
        form = EventForm(instance=event)

    return render(
        request,
        "customadmin/events/event_form.html",
        {"form": form, "event": event, "action_type": "update"},
    )


@login_required
def event_delete(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    messages.success(request, "Event deleted succussfully.")
    return redirect("events")


# ========================== END EVENT VIEWS ==========================


# ========================== EVENT POST VIEWS ==========================


@login_required
def eventposts(request):
    count = EventPost.objects.count()
    return render(
        request,
        "customadmin/eventposts/eventposts.html",
        {
            "count": count,
            "eventposts": EventPost.objects.all(),
        },
    )


@login_required
def eventposts_create(request):
    if request.method == "POST":
        form = EventPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New EventPost created succussfully.")
            return redirect("eventposts")
    else:
        form = EventPostForm()

    return render(request, "customadmin/eventposts/eventpost_form.html", {"form": form})


@login_required
def eventposts_update(request, id):
    eventposts = EventPost.objects.get(id=id)
    if request.method == "POST":
        form = EventPostForm(request.POST, request.FILES, instance=eventposts)
        if form.is_valid():
            form.save()
            messages.success(request, "EventPost updated succussfully.")
            return redirect("eventposts")
    else:
        form = EventPostForm(instance=eventposts)

    return render(
        request,
        "customadmin/eventposts/eventpost_form.html",
        {"form": form, "eventposts": eventposts, "action_type": "update"},
    )


@login_required
def eventposts_delete(request, id):
    eventposts = EventPost.objects.get(id=id)
    eventposts.delete()
    messages.success(request, "Event deleted succussfully.")
    return redirect("eventposts")


# ========================== END EVENT POST VIEWS ==========================


# ========================== BOOK VIEWS ==========================


@login_required
def books(request):
    count = Book.objects.count()
    low_stock_books = Book.objects.filter(quantity__lt=4)
    return render(
        request,
        "customadmin/books/books.html",
        {
            "count": count,
            "books": Book.objects.all(),
            "low_stock_books": low_stock_books,
        },
    )





from .utils import send_telegram_message

# @login_required
# def book_create(request):
#     if request.method == "POST":
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "New book created successfully.")
#             send_telegram_message("A new book has been created.")
#             return redirect("books")
#     else:
#         form = BookForm()

#     return render(request, "customadmin/books/book_form.html", {"form": form})

# @login_required
# def book_update(request, id):
#     book = Book.objects.get(id=id)
#     if request.method == "POST":
#         form = BookForm(request.POST, request.FILES, instance=book)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Book updated successfully.")
#             send_telegram_message(f"The book '{book.title}' has been updated.")
#             return redirect("books")
#     else:
#         form = BookForm(instance=book)

#     return render(request, "customadmin/books/book_form.html", {"form": form, "book": book, "action_type": "update"})


from django.contrib import messages
from .utils import send_telegram_message


@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, "New book created successfully.")
            # Notify if book quantity is less than 5
            if Book.quantity < 5:
                messages.warning(request, f"The quantity of the book '{Book.title}' is less than 5.")
                send_telegram_message(f"The quantity of the book '{Book.title}' is less than 5.")
            send_telegram_message("A new book has been created.")
            return redirect("books")
    else:
        form = BookForm()

    return render(request, "customadmin/books/book_form.html", {"form": form})

@login_required
def book_update(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, "Book updated successfully.")
            # Notify if book quantity is less than 5
            if book.quantity < 5:
                messages.warning(request, f"The quantity of the book '{book.title}' is less than 5.")
                send_telegram_message(f"The quantity of the book '{book.title}' is less than 5.")
            send_telegram_message(f"The book '{book.title}' has been updated.")
            return redirect("books")
    else:
        form = BookForm(instance=book)

    return render(request, "customadmin/books/book_form.html", {"form": form, "book": book, "action_type": "update"})

@login_required
def book_delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request, "book deleted succussfully.")
    return redirect("books")


# ========================== END book VIEWS ==========================







# ========================== Transaction VIEWS ==========================
from django.db.models import Sum, Count
from django.db.models.functions import TruncYear, TruncMonth, TruncWeek

@login_required
def transactions(request):
    count = Transaction.objects.count()
    transactions_by_year = Transaction.objects.annotate(year=TruncYear('payment_date')).values('year').annotate(total=Sum('amount_paid'), count=Count('id')).order_by('year')
    transactions_by_month = Transaction.objects.annotate(month=TruncMonth('payment_date')).values('month').annotate(total=Sum('amount_paid'), count=Count('id')).order_by('month')
    transactions_by_week = Transaction.objects.annotate(week=TruncWeek('payment_date')).values('week').annotate(total=Sum('amount_paid'), count=Count('id')).order_by('week')

    return render(
        request,
        "customadmin/transactions/transactions.html",
        {
            "count": count,
            "transactions": Transaction.objects.all(),
        'transactions_by_year': transactions_by_year,
        'transactions_by_month': transactions_by_month,
        'transactions_by_week': transactions_by_week,
        },
    )







# ========================== END book VIEWS ==========================

# ========================== Customer_Information VIEWS ==========================


@login_required
def WaliaPublishedBook(request):
    WaliaPublishedBook = Walia_Published_Book.objects.count()
    return render(
        request,
        "customadmin/WaliaPublishedBook/WaliaPublishedBook.html",
        {
            "WaliaPublishedBook": WaliaPublishedBook,
            "WaliaPublishedBook": Walia_Published_Book.objects.all(),
        },
    )


@login_required
def WaliaPublishedBook_create(request):
    if request.method == "POST":
        form = Walia_Published_BookForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            message = f'title: {obj.title} \nDescription: {obj.description} \ndiscount_price: {obj.discount_price} \nimage: {obj.image} '
            email = list(Subscriber.objects.filter().values_list('email', flat=True))
            send_mail(
            subject="Thank you for subscribing to our newsletter!",
            message=message,
            from_email="hayuya617@gmail.com",
            recipient_list=email,
        )

            messages.success(request, "New Waliapublishedbook created succussfully.")
            return redirect("WaliaPublishedBook")
    else:
        form = Walia_Published_BookForm()

    return render(
        request, "customadmin/WaliaPublishedBook/WaliaPublishedBook_form.html", {"form": form}
    )


@login_required
def WaliaPublishedBook_update(request, id):
    WaliaPublishedBook = Walia_Published_Book.objects.get(id=id)
    if request.method == "POST":
        form = Walia_Published_BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "WaliaPublishedBook updated succussfully.")
            return redirect("Walia_Published_Book")
    else:
        form = Walia_Published_BookForm(instance=WaliaPublishedBook)

    return render(
        request,
        "customadmin/WaliaPublishedBook/WaliaPublishedBook_form.html",
        {"form": form, "WaliaPublishedBook": WaliaPublishedBook, "action_type": "update"},
    )


@login_required
def WaliaPublishedBook_delete(request, id):
    WaliaPublishedBook = Walia_Published_Book.objects.get(id=id)
    WaliaPublishedBook.delete()
    messages.success(request, "WaliaPublishedBook deleted succussfully.")
    return redirect("WaliaPublishedBook")


# ========================== END Customer_Information VIEWS ==========================



# ========================== Customer_Information VIEWS ==========================


@login_required
def customer_info(request):
    customer_info = Customer_Information.objects.count()
    return render(
        request,
        "customadmin/customer_info/customer_info.html",
        {
            "customer_info": customer_info,
            "customer_info": Customer_Information.objects.all(),
        },
    )


@login_required
def customer_info_create(request):
    if request.method == "POST":
        form = Customer_InformationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New customer_info created succussfully.")
            return redirect("customer_info")
    else:
        form = Customer_InformationForm()

    return render(
        request, "customadmin/customer_info/customer_info_form.html", {"form": form}
    )


@login_required
def customer_info_update(request, id):
    customer_info = Customer_Information.objects.get(id=id)
    if request.method == "POST":
        form = Customer_InformationForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer_Information updated succussfully.")
            return redirect("customer_info")
    else:
        form = Customer_InformationForm(instance=customer_info)

    return render(
        request,
        "customadmin/customer_info/customer_info_form.html",
        {"form": form, "customer_info": customer_info, "action_type": "update"},
    )


@login_required
def customer_info_delete(request, id):
    customer_info = Customer_Information.objects.get(id=id)
    customer_info.delete()
    messages.success(request, "customer_info deleted succussfully.")
    return redirect("customer_info")


# ========================== END Customer_Information VIEWS ==========================


# ========================== Cart VIEWS ==========================


@login_required
def Cart(request):
    count = Cart.objects.count()
    return render(
        request,
        "customadmin/Cart/Cart.html",
        {
            "count": count,
            "Cart": Cart.objects.all(),
        },
    )


@login_required
def Cart_create(request):
    if request.method == "POST":
        form = CartForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New Cart created succussfully.")
            return redirect("Cart")
    else:
        form = CartForm()

    return render(request, "customadmin/Cart/Cart_form.html", {"form": form})


@login_required
def Cart_update(request, id):
    Cart = Cart.objects.get(id=id)
    if request.method == "POST":
        form = CartForm(request.POST, request.FILES, instance=Cart)
        if form.is_valid():
            form.save()
            messages.success(request, "Cart updated succussfully.")
            return redirect("Cart")
    else:
        form = CartForm(instance=Cart)

    return render(
        request,
        "customadmin/Cart/Cart_form.html",
        {"form": form, "Cart": Cart, "action_type": "update"},
    )


@login_required
def Cart_delete(request, id):
    Cart = Cart.objects.get(id=id)
    Cart.delete()
    messages.success(request, "Cart deleted succussfully.")
    return redirect("Cart")


# ========================== END cart VIEWS ==========================


# ========================== ConsignmentAgreemen VIEWS ==========================


@login_required
def ConsignmentAgreements(request):
    count = ConsignmentAgreement.objects.count()
    return render(
        request,
        "customadmin/ConsignmentAgreements/ConsignmentAgreements.html",
        {
            "count": count,
            "ConsignmentAgreements": ConsignmentAgreement.objects.all(),
        },
    )


@login_required
def ConsignmentAgreement_create(request):
    if request.method == "POST":
        form = ConsignmentAgreementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New Consignment Agreement created successfully.")
            return redirect("ConsignmentAgreements")
    else:
        form = ConsignmentAgreementForm()

    return render(
        request,
        "customadmin/ConsignmentAgreements/ConsignmentAgreement_form.html",
        {"form": form},
    )


@login_required
def ConsignmentAgreement_update(request, id):
    consignment_agreement = ConsignmentAgreement.objects.get(id=id)
    if request.method == "POST":
        form = ConsignmentAgreementForm(
            request.POST, request.FILES, instance=consignment_agreement
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Consignment Agreement updated successfully.")
            return redirect("ConsignmentAgreements")
    else:
        form = ConsignmentAgreementForm(instance=consignment_agreement)

    return render(
        request,
        "customadmin/ConsignmentAgreements/ConsignmentAgreement_form.html",
        {
            "form": form,
            "ConsignmentAgreement": consignment_agreement,
            "action_type": "update",
        },
    )


@login_required
def ConsignmentAgreement_delete(request, id):
    consignment_agreement = ConsignmentAgreement.objects.get(id=id)
    consignment_agreement.delete()
    messages.success(request, "Consignment Agreement deleted successfully.")
    return redirect("ConsignmentAgreements")


# ========================== END ConsignmentAgreement VIEWS ==========================


# ========================== AudioBookS VIEWS ==========================


@login_required
def AudioBookss(request):
    count = AudioBookS.objects.count()
    return render(
        request,
        "customadmin/AudioBookss/AudioBookss.html",
        {
            "count": count,
            "AudioBookss": AudioBookS.objects.all(),
        },
    )





# 





from .utils import send_telegram_message

@login_required
def AudioBookss_create(request):
    if request.method == "POST":
        form = AudioBookSForm(request.POST, request.FILES)
        if form.is_valid():
            audiobook = form.save()
            messages.success(request, f"A new Audiobook '{audiobook.title}' has been created.",)
            send_telegram_message("A new Audiobook has been created.", audiobook.audio_file.path)
            return redirect("AudioBookss")
    else:
        form = AudioBookSForm()

    return render(request, "customadmin/AudioBookss/AudioBook_form.html", {"form": form})

@login_required
def AudioBookss_update(request, id):
    audiobook = AudioBookS.objects.get(id=id)
    if request.method == "POST":
        form = AudioBookSForm(request.POST, request.FILES, instance=audiobook)
        if form.is_valid():
            form.save()
            messages.success(request, "AudioBook updated successfully.")
            send_telegram_message(f"The Audiobook '{audiobook.title}' has been updated.", audiobook.audio_file.path)
            return redirect("AudioBookss")
    else:
        form = AudioBookSForm(instance=audiobook)

    return render(request, "customadmin/AudioBookss/AudioBook_form.html", {"form": form, "AudioBookss": audiobook, "action_type": "update"})




@login_required
def AudioBookss_update(request, id):
    audiobook = AudioBookS.objects.get(id=id)
    if request.method == "POST":
        form = AudioBookSForm(request.POST, request.FILES, instance=audiobook)
        if form.is_valid():
            audiobook = form.save()
            messages.success(request, "AudioBook updated successfully.")
            
            # Send detailed information to Telegram
            send_telegram_message_with_media(
                f"The Audiobook '{audiobook.title}' has been updated.",
                audiobook.audio_file.url,
                audiobook.image.url if audiobook.image else None
            )
            return redirect("AudioBookss")
    else:
        form = AudioBookSForm(instance=audiobook)

    return render(request, "customadmin/AudioBookss/AudioBook_form.html", {"form": form, "AudioBookss": audiobook, "action_type": "update"})

@login_required
def AudioBookss_delete(request, id):
    AudioBookss = AudioBookS.objects.get(id=id)
    AudioBookss.delete()
    messages.success(request, "AudioBookS deleted succussfully.")
    return redirect("AudioBookss")


# ========================== END AudioBookS VIEWS ==========================





import os
import telebot
from django.shortcuts import render
from django.db.models import Q
from telebot import types


def telegram_bot(request):
    # Retrieve the bot token from environment variables
    BOT_TOKEN = os.environ.get('7486348793:AAEFA0AcY4Iw7oQIuzfCf-bjnTdyBwzptMk')
    bot = telebot.TeleBot('7486348793:AAEFA0AcY4Iw7oQIuzfCf-bjnTdyBwzptMk')

    @bot.message_handler(commands=['start', 'hello'])
    def send_welcome(message):
        bot.reply_to(message, '''
        Welcome to the Walia BookStore Bot!
        You can use the following commands:
        /category : Get a list of book categories
        /search <category_name> : Search books by category
        ''')
    

    @bot.message_handler(commands=['category'])
    def send_category(message):
        category_list = list(BookCategory.objects.all().values_list('name', flat=True))
        cat = ''
        for i in category_list:
            cat+=f"/{i} \n"
        bot.reply_to(message,cat) 
    

    @bot.message_handler (content_types = ['text'])
    def book_lists (message):
        text = message.text.replace('/', '')
        books = Book.objects.filter(Q(category__name__contains = text))
        book = []

        for i in books:


            detail = f'Title: {i.title} \nAuthor: {i.author} \nPrice: {i.price} \nDiscount: {i.discount_price} \nDescription: {i.description}'
            bot.reply_to(message, detail)
            #ebook = types.InputFile(EBook.objects.filter()[3].file.url)
            #bot.send_document(message.chat.id, ebook)
        

    

    bot.polling(non_stop=True, interval=0)

    # Return a template if needed, though the bot will keep running in the background
    return HttpResponse('Done')

# ========================== PDFDocument VIEWS ==========================


@login_required
def EBooks(request):
    count = EBook.objects.count()
    return render(
        request,
        "customadmin/EBooks/EBooks.html",
        {
            "count": count,
            "EBooks": EBook.objects.all(),
        },
    )



# from .utils import send_telegram_message

# @login_required
# def EBooks_create(request):
#     if request.method == "POST":
#         form = EBookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "New EBook created successfully.")
#             send_telegram_message("A new EBook has been created.")
#             return redirect("EBooks")
#     else:
#         form = EBookForm()

#     return render(request, "customadmin/EBooks/EBook_form.html", {"form": form})

# @login_required
# def EBooks_update(request, id):
#     EBooks = EBook.objects.get(id=id)
#     if request.method == "POST":
#         form = EBookForm(request.POST, request.FILES, instance=EBooks)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "EBook updated successfully.")
#             send_telegram_message(f"The EBook '{EBooks.title}' has been updated.")
#             return redirect("EBooks")
#     else:
#         form = EBookForm(instance=EBooks)

#     return render(request, "customadmin/EBooks/EBook_form.html", {"form": form, "EBooks": EBooks, "action_type": "update"})


from .utils import send_telegram_message

@login_required
def EBooks_create(request):
    if request.method == "POST":
        form = EBookForm(request.POST, request.FILES)
        if form.is_valid():
            ebook = form.save()
            messages.success(request, "New EBook created successfully.")
            send_telegram_message("A new EBook has been created.", ebook.file.path)
            return redirect("EBooks")
    else:
        form = EBookForm()

    return render(request, "customadmin/EBooks/EBook_form.html", {"form": form})

@login_required
def EBooks_update(request, id):
    ebook = EBook.objects.get(id=id)
    if request.method == "POST":
        form = EBookForm(request.POST, request.FILES, instance=ebook)
        if form.is_valid():
            form.save()
            messages.success(request, "EBook updated successfully.")
            send_telegram_message(f"The EBook '{ebook.title}' has been updated.", ebook.file.path ,)
            return redirect("EBooks")
    else:
        form = EBookForm(instance=ebook)

    return render(request, "customadmin/EBooks/EBook_form.html", {"form": form, "EBooks": ebook, "action_type": "update"})


@login_required
def EBooks_delete(request, id):
    EBooks = EBook.objects.get(id=id)
    EBooks.delete()
    messages.success(request, "EBooks deleted succussfully.")
    return redirect("EBooks")


# ========================== END PDFDocument VIEWS ==========================


# ========================== EventPostImage VIEWS ==========================


@login_required
def EventPostImages(request):
    count = EventPostImage.objects.count()
    return render(
        request,
        "customadmin/EventPostImages/EventPostImages.html",
        {
            "count": count,
            "EventPostImages": EventPostImage.objects.all(),
        },
    )


@login_required
def EventPostImage_create(request):
    if request.method == "POST":
        form = EventPostImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New EventPostImage created succussfully.")
            return redirect("EventPostImages")
    else:
        form = EventPostImageForm()

    return render(
        request, "customadmin/EventPostImages/EventPostImage_form.html", {"form": form}
    )


@login_required
def EventPostImage_update(request, id):
    EventPostImage = EventPostImage.objects.get(id=id)
    if request.method == "POST":
        form = EventPostImageForm(request.POST, request.FILES, instance=EventPostImage)
        if form.is_valid():
            form.save()
            messages.success(request, "EventPostImage updated succussfully.")
            return redirect("EventPostImages")
    else:
        form = EventPostImageForm(instance=EventPostImage)

    return render(
        request,
        "customadmin/EventPostImages/EventPostImage_form.html",
        {"form": form, "EventPostImage": EventPostImage, "action_type": "update"},
    )


@login_required
def EventPostImage_delete(request, id):
    EventPostImage = EventPostImage.objects.get(id=id)
    EventPostImage.delete()
    messages.success(request, "EventPostImage deleted succussfully.")
    return redirect("EventPostImages")


# ========================== END EventPostImage VIEWS ==========================


# ========================== contact VIEWS ==========================


@login_required
def contacts(request):
    count = Contact.objects.count()
    return render(
        request,
        "customadmin/contacts/contact.html",
        {
            "count": count,
            "contacts": Contact.objects.all(),
        },
    )


@login_required
def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New contact created succussfully.")
            return redirect("contacts")
    else:
        form = ContactForm()

    return render(request, "customadmin/contacts/contact_form.html", {"form": form})


@login_required
def contact_update(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "contact updated succussfully.")
            return redirect("contacts")
    else:
        form = BookForm(instance=contact)

    return render(
        request,
        "customadmin/contacts/contact_form.html",
        {"form": form, "contact": contact, "action_type": "update"},
    )


@login_required
def contact_delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    messages.success(request, "contact deleted succussfully.")
    return redirect("contact")


# ========================== END contact VIEWS ==========================

# ========================== AudioBooks VIEWS ==========================


@login_required
def AudioBook(request):
    count = AudioBookS.objects.count()
    return render(
        request,
        "customadmin/AudioBooks/AudioBooks.html",
        {
            "count": count,
            "AudioBookss": AudioBookS.objects.all(),
        },
    )


@login_required
def AudioBook_create(request):
    if request.method == "POST":
        form = AudioBookSForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New AudioBook created succussfully.")
            return redirect("AudioBook")
    else:
        form = AudioBookSForm()

    return render(request, "customadmin/AudioBooks/AudioBook_form.html", {"form": form})


@login_required
def AudioBook_update(request, id):
    AudioBook = AudioBookS.objects.get(id=id)
    if request.method == "POST":
        form = AudioBookSForm(request.POST, request.FILES, instance=AudioBook)
        if form.is_valid():
            form.save()
            messages.success(request, "AudioBooks updated succussfully.")
            return redirect("AudioBook")
    else:
        form = AudioBookSForm(instance=AudioBook)

    return render(
        request,
        "customadmin/AudioBook/AudioBook_form.html",
        {"form": form, "AudioBook": AudioBook, "action_type": "update"},
    )


@login_required
def AudioBook_delete(request, id):
    AudioBook = AudioBookS.objects.get(id=id)
    AudioBook.delete()
    messages.success(request, "AudioBook deleted succussfully.")
    return redirect("AudioBook")


# ========================== END book VIEWS ==========================


# ========================== blog VIEWS ==========================


@login_required
def blogs(request):
    count = Blog.objects.count()
    return render(
        request,
        "customadmin/blogs/blogs.html",
        {
            "count": count,
            "blogs": Blog.objects.all(),
        },
    )


from django.core.mail import send_mail

@login_required
def blog_create(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            message = f'title: {obj.title} \nDescription: {obj.description} \nmonth: {obj.month} \ncreated: {obj.created} '
            email = list(Subscriber.objects.filter().values_list('email', flat=True))
            send_mail(
            subject="Thank you for subscribing to our newsletter!",
            message=message,
            from_email="hayuya617@gmail.com",
            recipient_list=email,
        )

            messages.success(request, "New Blog created succussfully.")
            return redirect("blogs")
    else:
        form = BlogForm()

    return render(request, "customadmin/blogs/blog_form.html", {"form": form})


@login_required
def blog_update(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "blog updated succussfully.")
            return redirect("blogs")
    else:
        form = BookForm(instance=blog)

    return render(
        request,
        "customadmin/blogs/blog_form.html",
        {"form": form, "blog": blog, "action_type": "update"},
    )


@login_required
def blog_delete(request, id):
    Blog = Blog.objects.get(id=id)
    Blog.delete()
    messages.success(request, "Blog deleted succussfully.")
    return redirect("blogs")


# ========================== END blog VIEWS ==========================


# ========================== Author VIEWS ==========================


@login_required
def Authors(request):
    count = Author.objects.count()
    return render(
        request,
        "customadmin/Authors/Authors.html",
        {
            "count": count,
            "Authors": Author.objects.all(),
        },
    )


@login_required
def Authors_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New Author created succussfully.")
            return redirect("Authors")
    else:
        form = AuthorForm()

    return render(request, "customadmin/Authors/Author_form.html", {"form": form})


@login_required
def Authors_update(request, id):
    Authors = Author.objects.get(id=id)
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=Authors)
        if form.is_valid():
            form.save()
            messages.success(request, "Author updated succussfully.")
            return redirect("Authors")
    else:
        form = AuthorForm(instance=Authors)

    return render(
        request,
        "customadmin/Authors/Author_form.html",
        {"form": form, "Authors": Authors, "action_type": "update"},
    )


@login_required
def Authors_delete(request, id):
    Authors = Author.objects.get(id=id)
    Authors.delete()
    messages.success(request, "Author deleted succussfully.")
    return redirect("Authors")


# ========================== END Author VIEWS ==========================


# ========================== BookCategory VIEWS ==========================


@login_required
def BookCategorys(request):
    count = BookCategory.objects.count()
    return render(
        request,
        "customadmin/BookCategorys/BookCategorys.html",
        {
            "count": count,
            "BookCategorys": BookCategory.objects.all(),
        },
    )


@login_required
def BookCategorys_create(request):
    if request.method == "POST":
        form = BookCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New Author created succussfully.")
            return redirect("BookCategorys")
    else:
        form = BookCategoryForm()

    return render(
        request, "customadmin/BookCategorys/BookCategory_form.html", {"form": form}
    )


@login_required
def BookCategorys_update(request, id):
    BookCategorys = BookCategory.objects.get(id=id)
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=BookCategorys)
        if form.is_valid():
            form.save()
            messages.success(request, "BookCategory updated succussfully.")
            return redirect("BookCategorys")
    else:
        form = AuthorForm(instance=BookCategorys)

    return render(
        request,
        "customadmin/BookCategorys/BookCategory_form.html",
        {"form": form, "BookCategorys": BookCategorys, "action_type": "update"},
    )


@login_required
def BookCategorys_delete(request, id):
    BookCategorys = BookCategory.objects.get(id=id)
    BookCategorys.delete()
    messages.success(request, "BookCategorys deleted succussfully.")
    return redirect("BookCategorys")


# ========================== END BookCategory VIEWS ==========================


# ========================== BookCategory VIEWS ==========================


@login_required
def BookLanaguages(request):
    count = BookLanaguage.objects.count()
    return render(
        request,
        "customadmin/BookLanaguages/BookLanaguages.html",
        {
            "count": count,
            "BookLanaguages": BookLanaguage.objects.all(),
        },
    )


@login_required
def BookLanaguages_create(request):
    if request.method == "POST":
        form = BookLanaguageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "New BookLanaguage created succussfully.")
            return redirect("BookLanaguages")
    else:
        form = BookLanaguageForm()

    return render(
        request, "customadmin/BookLanaguages/BookLanaguage_form.html", {"form": form}
    )


@login_required
def BookLanaguages_update(request, id):
    BookLanaguages = BookLanaguage.objects.get(id=id)
    if request.method == "POST":
        form = BookLanaguageForm(request.POST, request.FILES, instance=BookLanaguage)
        if form.is_valid():
            form.save()
            messages.success(request, "BookLanaguage updated succussfully.")
            return redirect("BookLanaguages")
    else:
        form = BookLanaguageForm(instance=BookLanaguages)

    return render(
        request,
        "customadmin/BookLanaguages/BookLanaguage_form.html",
        {"form": form, "BookLanaguages": BookLanaguages, "action_type": "update"},
    )


@login_required
def BookLanaguages_delete(request, id):
    BookLanaguages = BookLanaguage.objects.get(id=id)
    BookLanaguages.delete()
    messages.success(request, "BookLanaguages deleted succussfully.")
    return redirect("BookLanaguages")


# ========================== END BookLanaguage VIEWS ==========================



