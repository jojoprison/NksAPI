from django.conf.urls import url
from CatalogueApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^products$', views.product_api),
    url(r'^products/([0-9]+)$', views.product_api),

    url(r'^products/save_file$', views.save_file),

    url(r'^types$', views.type_api),
    url(r'^types/([0-9]+)$', views.type_api)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
