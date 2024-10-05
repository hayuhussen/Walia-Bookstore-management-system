from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="index"),
    path("index2/", views.index2, name="index2"),
    path("contact/", views.contact, name="contact"),
    path("booksmediadetailv1/", views.booksmediadetailv1, name="booksmediadetailv1"),
    path("transactions/", views.transactions, name="transactions"),
    path("booksmediadetailv2/", views.booksmediadetailv2, name="booksmediadetailv2"),
    path(
        "booksmediagirdviewv1/", views.booksmediagirdviewv1, name="booksmediagirdviewv1"
    ),
    path(
        "booksmediagirdviewv2/", views.booksmediagirdviewv2, name="booksmediagirdviewv2"
    ),
    path("booksmedialistview/", views.booksmedialistview, name="booksmedialistview"),
    path("gallery/", views.gallery, name="gallery"),
    path("homev2/", views.homev2, name="homev2"),
    path("homev3/", views.homev3, name="homev3"),
    path("services/", views.services, name="services"),
    path("newseventsdetail/<int:id>/", views.newseventsdetail, name="newseventsdetail"),
    path("newseventslistview/", views.newseventslistview, name="newseventslistview"),
    path("404/", views.a404, name="404"),
    path("blogdetail/<int:id>/", views.blogdetail, name="blogdetail"),
    path("blog/", views.blog, name="blog"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("signin/", views.signin, name="signin"),
    path("event/", views.event, name="event"),
    path("ebook/", views.ebook, name="ebook"),
    path("audio/", views.audio, name="audio"),
    path("footer/", views.footer, name="footer"),
    path("history/", views.history, name="history"),
    path("create_post/", views.create_post, name="create_post"),
]
