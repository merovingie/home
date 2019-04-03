from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('jobs.urls')),
    path('blog/',include('blog.urls')),
    path('todo/',include('todo.urls')),
    path('accounts/',include('accounts.urls')),
    path('skills/',include('skills.urls')),
    path('json/',include('restapi.urls')),
    path('pijson/',include('djangoendpoint.urls')),
    path('histology/',include('Histology.urls')),
]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 

