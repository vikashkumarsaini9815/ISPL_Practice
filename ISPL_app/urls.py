from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path("admin/", admin.site.urls),
    path("allinfo/", All_infoAPIView.as_view(),name='allifoAPIView'),
    path("registration/", RegistrationAPIView.as_view(),name='registration')
]
