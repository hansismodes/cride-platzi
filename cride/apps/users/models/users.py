# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

# Utilities
from apps.utils.models import CRideModel

class User(CRideModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_number = models.CharField(
        validators= [
            validators.RegexValidator(regex = r'\+?1?\d{9,15}$'),
        ], 
        max_length=17, 
        blank=True, 
        verbose_name = "Teléfono"
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to true when the user have verified its email address.'
    )

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""
        return self.username