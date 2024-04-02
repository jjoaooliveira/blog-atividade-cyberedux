from django.contrib import admin
from django.urls import include, path
from blog import views as bviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', bviews.home, name='home'),
    path('post/', bviews.create_post, name='create_post'),
    path('<slug:slug>/', bviews.post_details, name='post_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)