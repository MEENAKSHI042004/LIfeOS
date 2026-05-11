from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('apps.accounts.urls')),
    path('api/analytics_app/', include('apps.analytics_app.urls')),
    path('api/habits/', include('apps.habits.urls')),
    path('api/goals/', include('apps.goals.urls')),
    path('api/finance/', include('apps.finance.urls')),
]