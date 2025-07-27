from django.urls import path
# --- FIX: Import all the necessary views from views.py ---
from .views import CustomTokenObtainPairView, UserProfileView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Existing endpoints
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoints for profile and logout
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
