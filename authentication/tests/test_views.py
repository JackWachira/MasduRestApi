"""Import test tools from rest_framework."""

from rest_framework.test import APITestCase


class AuthenticationTestCase(APITestCase):
    """Tests Signup and Login"""

    def test_registration_successful(self):
        """Test that new user is registered successfully"""
        creation_response = self.client.post('/api/auth/register/',
                                             {
                                                 'username': 'jack',
                                                 'email': 'jack@gmail.com',
                                                 'password': '12345',
                                             },
                                             format='json')
        self.assertEqual(creation_response.status_code, 201)

    def test_unsuccesful_registration(self):
        """Test that an existing user canot register more than once"""
        creation_response = self.client.post('/api/auth/register/',
                                             {
                                                 'username': 'jack',
                                                 'email': 'jack@gmail.com',
                                                 'password': '12345',
                                             },
                                             format='json')
        self.assertEqual(creation_response.status_code, 201)
        response = self.client.post('/api/auth/register/',
                                    {
                                        'username': 'jack',
                                        'email': 'jack@gmail.com',
                                        'password': '12345',
                                    },
                                    format='json')
        self.assertEqual(response.status_code, 400)

    def test_authorization_returns_a_token(self):
        """Test that correct login details return a token."""
        response = self.client.post('/api/auth/register/',
                                    {
                                        'username': 'jack',
                                        'email': 'jack@gmail.com',
                                        'password': '12345',
                                    },
                                    format='json')

        response = self.client.post('/api/auth/login/',
                                    {
                                        'username': 'jack@gmail.com',
                                        'password': '12345',
                                    },
                                    format='json')

        self.assertIn("token", response.data)

    def test_unathorised_user_cannot_login(self):
        """Test that unauthorised user cannot login"""
        response = self.client.post('/api/auth/register/',
                                    {
                                        'username': 'jack',
                                        'email': 'jack@gmail.com',
                                        'password': '12345',
                                    },
                                    format='json')

        response = self.client.post('/api/auth/login/',
                                    {
                                        'username': 'tom@gmail.com',
                                        'password': '12345',
                                    },
                                    format='json')

        self.assertEqual(response.status_code, 400)
