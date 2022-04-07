from django.conf.urls import url
from django.urls import path

from CatalogueApp import views

from django.conf.urls.static import static
from django.conf import settings

from CatalogueApp.views import ProductViewSet, TableViewSet, ChairViewSet, DrawerViewSet, StandViewSet, RackViewSet, \
    AccessoryViewSet

urlpatterns = [
    # url(r'^products$', views.product_api),
    # url(r'^products/([0-9]+)$', views.product_api),
    #
    # url(r'^product/([0-9]+)$', views.product_detail_api),
    #
    # url(r'^products/filtersAll$', views.product_filter_all_api),
    path('products/filtersAll', views.products_fields_values),
    path('products/filter', views.products_filtered),
    path('tables/filtersAll', views.tables_fields_values),
    path('tables/filter', views.tables_filtered),
    path('chairs/filtersAll', views.chairs_fields_values),
    path('chairs/filter', views.chairs_filtered),
    path('drawers/filtersAll', views.drawers_fields_values),
    path('drawers/filter', views.drawers_filtered),
    path('stands/filtersAll', views.stands_fields_values),
    path('stands/filter', views.stands_filtered),
    path('racks/filtersAll', views.racks_fields_values),
    path('racks/filter', views.racks_filtered),
    path('accessories/filtersAll', views.accessories_fields_values),
    path('accessories/filter', views.accessories_filtered),

    # url(r'^client$', views.client_api),
    #
    # url(r'^order$', views.order_api),
    #
    # url(r'^types$', views.type_api),
    # url(r'^types/([0-9]+)$', views.type_api),

    path('products/', ProductViewSet.as_view({'get': 'list'})),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('tables/', TableViewSet.as_view({'get': 'list'})),
    path('tables/<int:pk>/', TableViewSet.as_view({'get': 'retrieve'})),
    path('chairs/', ChairViewSet.as_view({'get': 'list'})),
    path('chairs/<int:pk>/', ChairViewSet.as_view({'get': 'retrieve'})),
    path('drawers/', DrawerViewSet.as_view({'get': 'list'})),
    path('drawers/<int:pk>/', DrawerViewSet.as_view({'get': 'retrieve'})),
    path('stands/', StandViewSet.as_view({'get': 'list'})),
    path('stands/<int:pk>/', StandViewSet.as_view({'get': 'retrieve'})),
    path('racks/', RackViewSet.as_view({'get': 'list'})),
    path('racks/<int:pk>/', RackViewSet.as_view({'get': 'retrieve'})),
    path('accessories/', AccessoryViewSet.as_view({'get': 'list'})),
    path('accessories/<int:pk>/', AccessoryViewSet.as_view({'get': 'retrieve'})),
    # шкафы пока не делаем
    # path('cabinets/', ProductViewSet.as_view({'get': 'list'})),
    # path('cabinets/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    # path('types$/', ProductViewSet.as_view({'get': 'list'})),
    # path('types/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    # path('subtypes/', ProductViewSet.as_view({'get': 'list'})),
    # path('subtypes/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('order/', views.order_api),

    # пока не нужен, мб в будущем когда ЛК будет
    # path('client/', ProductViewSet.as_view({'get': 'list'})),
]
