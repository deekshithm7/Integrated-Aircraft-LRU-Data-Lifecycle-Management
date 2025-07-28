from django.urls import path

from .views import CustomTokenObtainPairView, UserProfileView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView


from .views import (
    CustomTokenObtainPairView,
    UserProfileView,
    LogoutView,
    ChangePasswordView,
    ActiveSessionsView,
    TerminateSessionView
)



urlpatterns = [
    
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),

    path('sessions/', ActiveSessionsView.as_view(), name='active_sessions'),
    path('sessions/<int:pk>/terminate/', TerminateSessionView.as_view(), name='terminate_session'),
]
