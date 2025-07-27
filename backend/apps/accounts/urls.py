from django.urls import path
# --- FIX: Import all the necessary views from views.py ---
from .views import CustomTokenObtainPairView, UserProfileView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

# --- FIX: Import the new view ---
from .views import (
    CustomTokenObtainPairView,
    UserProfileView,
    LogoutView,
    ChangePasswordView,
    ActiveSessionsView,
    TerminateSessionView
)



urlpatterns = [
    # Existing endpoints
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoints for profile and logout
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    path('sessions/', ActiveSessionsView.as_view(), name='active_sessions'),
    path('sessions/<int:pk>/terminate/', TerminateSessionView.as_view(), name='terminate_session'),
]
