from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from CatalogueApp.urls import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),


    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('CatalogueApp.urls')),
    path('', include('auth_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
