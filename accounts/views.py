from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    UserCreateSerializer,
    UserSerializer,
    UserUpadateSerializer,
)

User = get_user_model()


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return UserCreateSerializer
        return self.serializer_class


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    http_method_names = ["get", "patch", "delete"]
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "PATCH":
            return UserUpadateSerializer
        return self.serializer_class
