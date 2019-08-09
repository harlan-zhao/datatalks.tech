from django.urls import path,include
from .views import UserView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',UserView)


urlpatterns = [
    path('',include(router.urls))
]
 