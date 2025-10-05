from django.urls import path
from website.views import *

urlpatterns = [
    path("", home_view),
    path("support", support_view),
    path("about", about_view)
]