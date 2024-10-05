from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customadmin.views import telegram_bot


urlpatterns = [
    # path("jet/", include("jet.urls", "jet")),
    # path(
    #     "jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")
    # ),  # Django JET dashboard URLS
    path("oldadmin/", admin.site.urls),
    # yeha aykerem
    path("", include("Campany.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("accounts/", include("allauth.urls")),
    path("admin/", include("customadmin.urls")),
    path("telebot/", telegram_bot, name="telebot"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
