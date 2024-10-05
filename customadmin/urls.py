from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    # ====================== EVENT URLS =====================
    path("events/", views.events, name="events"),
    path("events/create/", views.event_create, name="event_create"),
    path("events/update/<int:id>/", views.event_update, name="event_update"),
    path("events/delete/<int:id>/", views.event_delete, name="event_delete"),
    # =======================================================
    # ====================== EVENT POST URLS =====================
    path("eventposts/", views.eventposts, name="eventposts"),
    path("eventposts/create/", views.eventposts_create, name="eventposts_create"),
    path(
        "eventposts/update/<int:id>/", views.eventposts_update, name="eventposts_update"
    ),
    path(
        "eventposts/delete/<int:id>/", views.eventposts_delete, name="eventposts_delete"
    ),
    # =======================================================
    # ====================== BOOK URLS =====================
    path("books/", views.books, name="books"),
    path("books/create/", views.book_create, name="book_create"),
    path("books/update/<int:id>/", views.book_update, name="book_update"),
    path("books/delete/<int:id>/", views.book_delete, name="book_delete"),
    # =======================================================


 # ====================== telebot URLS =====================
    path("transactions/", views.transactions, name="transactions"),
    
    # =======================================================


    # ====================== BOOK URLS =====================
    
    # =======================================================



    # ====================== WaliaPublishedBook URLS =====================
    path("WaliaPublishedBook/", views.WaliaPublishedBook, name="WaliaPublishedBook"),
    path(
        "WaliaPublishedBook/create/", views.WaliaPublishedBook_create, name="WaliaPublishedBook_create"
    ),
    path(
        "WaliaPublishedBook/update/<int:id>/",
        views.WaliaPublishedBook_update,
        name="WaliaPublishedBook_update",
    ),
    path(
        "WaliaPublishedBook/delete/<int:id>/",
        views.WaliaPublishedBook_delete,
        name="WaliaPublishedBook_delete",
    ),
    # ======================end WaliaPublishedBook================================



    # ====================== customer_info URLS =====================
    path("customer_info/", views.customer_info, name="customer_info"),
    path(
        "customer_info/create/", views.customer_info_create, name="customer_info_create"
    ),
    path(
        "customer_info/update/<int:id>/",
        views.customer_info_update,
        name="customer_info_update",
    ),
    path(
        "customer_info/delete/<int:id>/",
        views.customer_info_delete,
        name="customer_info_delete",
    ),
    # ======================end customer_info================================
    # ====================== BOOK URLS =====================
    path(
        "ConsignmentAgreements/",
        views.ConsignmentAgreements,
        name="ConsignmentAgreements",
    ),
    path(
        "ConsignmentAgreements/create/",
        views.ConsignmentAgreement_create,
        name="ConsignmentAgreement_create",
    ),
    path(
        "ConsignmentAgreements/update/<int:id>/",
        views.ConsignmentAgreement_update,
        name="ConsignmentAgreement_update",
    ),
    path(
        "ConsignmentAgreements/delete/<int:id>/",
        views.ConsignmentAgreement_delete,
        name="ConsignmentAgreement_delete",
    ),
    # =======================================================
    # ====================== cart URLS =====================
    path("Cart/", views.Cart, name="Cart"),
    path("Cart/create/", views.Cart_create, name="Cart_create"),
    path("Cart/update/<int:id>/", views.Cart_update, name="Cart_update"),
    path("Cart/delete/<int:id>/", views.Cart_delete, name="Cart_delete"),
    # =======================================================
    # ====================== AudioBook URLS =====================
    path("AudioBookss/", views.AudioBookss, name="AudioBookss"),
    path("AudioBookss/create/", views.AudioBookss_create, name="AudioBookss_create"),
    path(
        "AudioBookss/update/<int:id>/",
        views.AudioBookss_update,
        name="AudioBookss_update",
    ),
    path(
        "AudioBookss/delete/<int:id>/",
        views.AudioBookss_delete,
        name="AudioBookss_delete",
    ),
    # =======================================================
    # ====================== PDFDocument URLS =====================
    path("EBooks/", views.EBooks, name="EBooks"),
    path("EBooks/create/", views.EBooks_create, name="EBooks_create"),
    path(
        "EBooks/update/<int:id>/",
        views.EBooks_update,
        name="EBooks_update",
    ),
    path(
        "EBooks/delete/<int:id>/",
        views.EBooks_delete,
        name="EBooks_delete",
    ),
    # =======================================================
    # ====================== contacts URLS =====================
    path("contacts/", views.contacts, name="contacts"),
    path("contacts/create/", views.contact_create, name="contact_create"),
    path("contacts/update/<int:id>/", views.contact_update, name="contact_update"),
    path("contacts/delete/<int:id>/", views.contact_delete, name="contact_delete"),
    # =======================================================
    # ====================== EventPostImage URLS =====================
    path("EventPostImages/", views.EventPostImages, name="EventPostImages"),
    path(
        "EventPostImages/create/",
        views.EventPostImage_create,
        name="EventPostImage_create",
    ),
    path(
        "EventPostImages/update/<int:id>/",
        views.EventPostImage_update,
        name="EventPostImage_update",
    ),
    path(
        "EventPostImages/delete/<int:id>/",
        views.EventPostImage_delete,
        name="EventPostImage_delete",
    ),
    # =======================================================
    # ====================== AudioBook URLS =====================
    path("AudioBook/", views.AudioBook, name="AudioBook"),
    path("AudioBook/create/", views.AudioBook_create, name="AudioBook_create"),
    path("AudioBook/update/<int:id>/", views.AudioBook_update, name="AudioBook_update"),
    path("AudioBook/delete/<int:id>/", views.AudioBook_delete, name="AudioBook_delete"),
    # =======================================================
    # ====================== blog URLS =====================
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/create/", views.blog_create, name="blog_create"),
    path("blogs/update/<int:id>/", views.blog_update, name="Blog_update"),
    path("blogs/delete/<int:id>/", views.blog_delete, name="Blog_delete"),
    # =======================================================
    # ====================== Author URLS =====================
    path("Authors/", views.Authors, name="Authors"),
    path("Authors/create/", views.Authors_create, name="Authors_create"),
    path("Authors/update/<int:id>/", views.Authors_update, name="Authors_update"),
    path("Authors/delete/<int:id>/", views.Authors_delete, name="Authors_delete"),
    # =======================================================
    # ====================== BookCategory URLS =====================
    path("BookCategorys/", views.BookCategorys, name="BookCategorys"),
    path(
        "BookCategorys/create/", views.BookCategorys_create, name="BookCategorys_create"
    ),
    path(
        "BookCategorys/update/<int:id>/",
        views.BookCategorys_update,
        name="BookCategorys_update",
    ),
    path(
        "BookCategorys/delete/<int:id>/",
        views.BookCategorys_delete,
        name="BookCategorys_delete",
    ),
    # ====================== BookLanaguage URLS =====================
    path("BookLanaguages/", views.BookLanaguages, name="BookLanaguages"),
    path(
        "BookLanaguages/create/",
        views.BookLanaguages_create,
        name="BookLanaguages_create",
    ),
    path(
        "BookLanaguages/update/<int:id>/",
        views.BookLanaguages_update,
        name="BookLanaguages_update",
    ),
    path(
        "BookLanaguages/delete/<int:id>/",
        views.BookLanaguages_delete,
        name="BookLanaguages_delete",
    ),
    # ====================ends==BookLanaguage=============================
    
    # path('sales/', views.sales, name='sales'),
   
]
