from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from upload.views import UploadCreateView

urlpatterns = [
    path('', UploadCreateView.as_view(), name='upload'),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
