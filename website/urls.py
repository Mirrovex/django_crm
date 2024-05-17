from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('record/<int:id>/', customer_record, name='record'),
    path('delete/<int:id>/', delete_record, name='delete'),
]
