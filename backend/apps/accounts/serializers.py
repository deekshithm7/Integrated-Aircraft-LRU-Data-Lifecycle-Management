from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims from the prompt
        token['role'] = user.role
        token['can_approve_installations'] = user.can_approve_installations
        token['can_override_validations'] = user.can_override_validations

        permissions = list(user.get_all_permissions())
        token['permissions'] = permissions

        return token

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'employee_id', 'department', 'phone_number',
            'aircraft_certifications',
            'can_approve_installations', 'can_override_validations',
            'last_login'
        ]
        # Users can't change these fields for themselves
        read_only_fields = [
            'id', 'username', 'role', 'last_login',
            'can_approve_installations', 'can_override_validations'
        ]
