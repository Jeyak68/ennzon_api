from django.urls import path
from .views import add_service, add_ads, \
    get_users, add_banner, add_category, edit_category, category_list, delete_category, banner_list, edit_service, delete_service, service_list, add_image

urlpatterns = [
    path('add_service', add_service),
    path('edit_service', edit_service),
    path('delete_service', delete_service),
    path('service_list', service_list),
    path('add_ads', add_ads),
    path('get_users', get_users),
    path('add_banner', add_banner),
    path('banner_list', banner_list),
    path('add_category', add_category),
    path('edit_category', edit_category),
    path('category_list', category_list),
    path('delete_category', delete_category),
    path('add_image', add_image),
]
