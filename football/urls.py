from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/getactive/', ActiveProducts.as_view()),
    path('bot/getinactive/', InactiveProducts.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
