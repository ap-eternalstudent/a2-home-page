import os

from django.conf import settings
from django.conf.urls import handler404, handler500
from django.contrib import admin
from django.urls import path

from a2.components.pages.urls import urlpatterns as pages
from a2.components.pages.views import page_not_found, server_error


handler404 = page_not_found
handler500 = server_error

urlpatterns = []
urlpatterns += pages