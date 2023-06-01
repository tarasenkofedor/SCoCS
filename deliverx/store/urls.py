from django.urls import path

from .views import *

urlpatterns = [
    path('', page_main),
    path('login/', page_login)
]