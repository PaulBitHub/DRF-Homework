from django.urls import path
from users.apps import UsersConfig

from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserViewSet, PaymentViewSet, UserCreateApiView, PaymentDestroyApiView, PaymentUpdateApiView, \
    PaymentRetrieveApiView, PaymentListApiView, PaymentCreateApiView, UserListApiView, UserRetrieveApiView, \
    UserUpdateApiView, UserDestroyApiView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", viewset=UserViewSet, basename="users")
router.register(r"payment", viewset=PaymentViewSet, basename="payment")

urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path('payment/create/', PaymentCreateApiView.as_view(), name='payment-create'),
    path('payment/', PaymentListApiView.as_view(), name='payment-list'),
    path('payment/<int:pk>/', PaymentRetrieveApiView.as_view(), name='payment-retrieve'),
    path('payment/<int:pk>/update/', PaymentUpdateApiView.as_view(), name='payment-update'),
    path('payment/<int:pk>/delete/', PaymentDestroyApiView.as_view(), name='payment-delete'),
    path('users/create/', UserCreateApiView.as_view(), name='user-create'),
    path('users/', UserListApiView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveApiView.as_view(), name='user-retrieve'),
    path('users/<int:pk>/update/', UserUpdateApiView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDestroyApiView.as_view(), name='user-delete'),
] + router.urls
