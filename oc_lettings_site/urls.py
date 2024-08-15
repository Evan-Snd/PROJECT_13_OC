from django.contrib import admin
from profiles.views import profile, profiles_index
from letting.views import lettings_index, letting
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import settings as set
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('admin/', admin.site.urls),
]
handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)