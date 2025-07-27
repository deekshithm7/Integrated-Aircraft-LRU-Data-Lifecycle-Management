from rest_framework.permissions import BasePermission

class IsTechnician(BasePermission):
    """
    Allows access only to users with the 'TECHNICIAN' role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'TECHNICIAN'

class IsQAManager(BasePermission):
    """
    Allows access only to users with the 'QA_MANAGER' role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'QA_MANAGER'

class IsAdministrator(BasePermission):
    """
    Allows access only to users with the 'ADMINISTRATOR' role.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ADMINISTRATOR'

class CanOverrideValidations(BasePermission):
    """
    Allows access only to users who can override business rule validations.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.can_override_validations
