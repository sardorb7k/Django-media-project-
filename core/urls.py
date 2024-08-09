from django.contrib import admin
from django.urls import path
from blog.views import HomePage, UploadPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name='home'),
    path('upload/', UploadPage, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
