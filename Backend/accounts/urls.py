from rest_framework import routers
from accounts.views import *
from django.urls import path, include, re_path
import djoser

router = routers.DefaultRouter()
router.register('accounts', UserView)

urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^auth', include('djoser.urls.authtoken')),

]
