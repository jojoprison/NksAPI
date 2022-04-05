from django.conf.urls import url
from django.urls import path

from CatalogueApp import views

from django.conf.urls.static import static
from django.conf import settings

from CatalogueApp.views import ProductViewSet, TableViewSet

urlpatterns = [
    # url(r'^products$', views.product_api),
    # url(r'^products/([0-9]+)$', views.product_api),
    #
    # url(r'^product/([0-9]+)$', views.product_detail_api),
    #
    # url(r'^products/filtersAll$', views.product_filter_all_api),
    path('products/filtersAll', views.product_filter_all_api),
    path('products/filter', views.product_filter_api),

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
    # шкафы пока не делаем
    # path('cabinets/', ProductViewSet.as_view({'get': 'list'})),
    # path('cabinets/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('racks/', ProductViewSet.as_view({'get': 'list'})),
    path('racks/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('chairs/', ProductViewSet.as_view({'get': 'list'})),
    path('chairs/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('drawers/', ProductViewSet.as_view({'get': 'list'})),
    path('chairs/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('stands/', ProductViewSet.as_view({'get': 'list'})),
    path('stands/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('accessories/', ProductViewSet.as_view({'get': 'list'})),
    path('accessories/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),

    # path('types$/', ProductViewSet.as_view({'get': 'list'})),
    # path('types/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    # path('subtypes/', ProductViewSet.as_view({'get': 'list'})),
    # path('subtypes/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    path('order/', views.order_api),

    # пока не нужен, мб в будущем когда ЛК будет
    # path('client/', ProductViewSet.as_view({'get': 'list'})),
]
