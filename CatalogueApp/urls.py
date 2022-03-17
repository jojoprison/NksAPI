from django.conf.urls import url
from CatalogueApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^products$', views.product_api),
    url(r'^products/([0-9]+)$', views.product_api),

    url(r'^products/filtersAll$', views.product_filter_all_api),
    url(r'^products/filter$', views.product_filter_api),

    # TODO мб сделать маппинг просто на /save_file без привязки products
    url(r'^products/save_file$', views.save_file),

    url(r'^client$', views.client_api),

    url(r'^order$', views.order_api),

    url(r'^types$', views.type_api),
    url(r'^types/([0-9]+)$', views.type_api)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

