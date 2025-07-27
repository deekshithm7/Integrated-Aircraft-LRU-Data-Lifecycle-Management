from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('TECHNICIAN', 'Technician'),
        ('ADMINISTRATOR', 'Administrator'),
        ('QA_MANAGER', 'QA/Manager'),
    )

    # Basic fields
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='TECHNICIAN')
    employee_id = models.CharField(max_length=20, unique=True, null=True, blank=True)
    department = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    # LRU domain-specific fields from the prompt
    aircraft_certifications = models.JSONField(
        default=list,
        help_text="List of aircraft types user is certified for"
    )
    authorized_aircraft_types = models.JSONField(
        default=list,
        help_text="Aircraft types user can work on"
    )
    can_approve_installations = models.BooleanField(
        default=False,
        help_text="Can approve LRU installations"
    )
    can_override_validations = models.BooleanField(
        default=False,
        help_text="Can override business rule validations"
    )
    can_manage_trial_installations = models.BooleanField(
        default=False,
        help_text="Can manage one-off trial installations"
    )

    # Audit fields
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.username
