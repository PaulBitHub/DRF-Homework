from django.urls import path
from users.apps import UsersConfig

from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from users.views import UserViewSet, PaymentViewSet, UserCreateApiView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", viewset=UserViewSet, basename="users")
router.register(r"payment", viewset=PaymentViewSet, basename="payment")

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
] + router.urls
