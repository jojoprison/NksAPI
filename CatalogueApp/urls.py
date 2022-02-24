from django.conf.urls import url
from CatalogueApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # TODO заменить все на product
    url(r'^table$', views.product_api),
    url(r'^table/([0-9]+)$', views.product_api),

    url(r'^table/save_file$', views.save_file)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
