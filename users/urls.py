from django.urls import path
from users.apps import UsersConfig
from users.views import UserAuthenticationView, UserProfileView, VerificationView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = UsersConfig.name

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
    ),
    public=True,
)

urlpatterns = [
    path('verify/', VerificationView.as_view(), name='verification'),
    path('auth/', UserAuthenticationView.as_view(), name='user_authentication'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

]