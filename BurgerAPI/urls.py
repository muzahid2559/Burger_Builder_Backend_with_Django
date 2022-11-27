from django.urls import path
from BurgerAPI import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', views.UserProfileViewset)


urlpatterns = [] + router.urls