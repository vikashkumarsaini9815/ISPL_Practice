from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path("allinfo/", All_infoAPIView.as_view(),name='allifoAPIView'),
    path("registration_data/", registration_GET_APIView.as_view(),name='registration_data'),
   # path("registration_update/", Registration_updateAPIView.as_view(),name='registration_update'),
    path("registration/", RegistrationAPIView.as_view(),name='registration')
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 