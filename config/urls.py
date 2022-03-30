from django.contrib import admin
from django.urls import path, include
from celero.views import AthleteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'atlhetes', AthleteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
