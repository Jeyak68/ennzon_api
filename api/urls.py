from django.urls import path
from .views import add_decoration, add_caterers, add_ice_creams, add_makeup, add_venue, add_photography, add_ads, \
    get_users, add_banner, add_category, edit_category, category_list, delete_category, banner_list, edit_decoration, delete_decoration, decoration_list, add_image

urlpatterns = [
    path('add_decoration', add_decoration),
    path('edit_decoration', edit_decoration),
    path('delete_decoration', delete_decoration),
    path('decoration_list', decoration_list),
    path('add_caters', add_caterers),
    path('add_icecream', add_ice_creams),
    path('add_makeup', add_makeup),
    path('add_photography', add_photography),
    path('add_venue', add_venue),
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
