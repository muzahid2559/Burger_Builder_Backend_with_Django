from BurgerAPI.models import UserProfile, Order  # Model
from .serializers import UserProfileSerializer, OrderSerializer # serializer based on BurgerAPI model


# building features
from rest_framework import parsers, viewsets


# Create your views here.

class UserProfileViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
