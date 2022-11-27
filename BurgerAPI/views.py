from BurgerAPI.models import UserProfile # Model
from .serializers import UserProfileSerializer # serializer based on BurgerAPI model


# building features
from rest_framework import parsers, viewsets


# Create your views here.

class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer