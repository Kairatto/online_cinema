from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from accounts.views import MyObtainAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie.urls')),
    path('accounts/', include('accounts.urls')),
    path('auth/', include('rest_framework.urls')),
    path('token/', MyObtainAuthToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
