from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenBlacklistView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    # path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),

    # Auth Path
    # path("signup", Signup),
]