import pytest
from rest_framework.test import APIClient
from .models import User


pytestmark = pytest.mark.django_db


def test_user_login():
    """
    Tests that a user can successfully log in and receive JWT tokens.
    """
    client = APIClient()
    
    # Create a test user in the database
    User.objects.create_user(
        username='testuser',
        password='testpassword123',
        role='TECHNICIAN'
    )

    # Attempt to log in
    response = client.post('/api/v1/auth/login/', {
        'username': 'testuser',
        'password': 'testpassword123'
    }, format='json')

    # Assert that the request was successful
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data

def test_get_profile_unauthenticated():
    """
    Tests that an unauthenticated user cannot access the profile endpoint.
    """
    client = APIClient()
    response = client.get('/api/v1/auth/profile/')
    
    
    assert response.status_code == 401

def test_get_profile_authenticated():
    """
    Tests that an authenticated user can retrieve their profile.
    """
    client = APIClient()
    user = User.objects.create_user(username='authtest', password='password123')
    
    
    client.force_authenticate(user=user)
    
    response = client.get('/api/v1/auth/profile/')
    
    
    assert response.status_code == 200
    assert response.data['username'] == 'authtest'

def test_update_profile():
    """
    Tests that a user can update their own profile.
    """
    client = APIClient()
    user = User.objects.create_user(
        username='updatetest',
        password='password123',
        first_name='Original'
    )
    client.force_authenticate(user=user)
    
    
    response = client.put('/api/v1/auth/profile/', {
        'first_name': 'Updated',
        'last_name': 'Name'
    }, format='json')
    
    
    assert response.status_code == 200
    assert response.data['first_name'] == 'Updated'
    
    
    user.refresh_from_db()
    assert user.first_name == 'Updated'
