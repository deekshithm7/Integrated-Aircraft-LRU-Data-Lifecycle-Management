from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User, UserSession # <-- ADD UserSession

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super().validate(attrs)

        # Get the refresh token object
        refresh = self.get_token(self.user)

        # Extract jti (JWT ID) from the refresh token
        jti = refresh.payload.get('jti')

        # Get IP and User Agent from the request
        request = self.context['request']
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        # Create the user session record
        UserSession.objects.create(
            user=self.user,
            refresh_token_jti=jti,
            ip_address=ip_address,
            user_agent=user_agent
        )

        return data

    @classmethod
    def get_token(cls, user):
        # This method remains the same
        token = super().get_token(user)
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
        read_only_fields = [
            'id', 'username', 'role', 'last_login',
            'can_approve_installations', 'can_override_validations'
        ]

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError({"new_password": "New passwords must match."})
        validate_password(data['new_password'])
        return data

class UserSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSession
        fields = ['id', 'ip_address', 'user_agent', 'last_seen']
