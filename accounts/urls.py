from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

from . import views

app_name = "accounts"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("", views.UserListCreateAPIView.as_view(), name="users"),
    path(
        "<uuid:pk>/",
        views.UserRetrieveUpdateDestroyAPIView.as_view(),
        name="user",
    ),
]
