from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile


class UserViewsTests(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        self.test_user.save()
        
        # User profile should be automatically created via signals
        self.profile = UserProfile.objects.get(user=self.test_user)
    
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_menu_view(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
    
    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
    
    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
    
    def test_login_functionality(self):
        # Test login process
        login = self.client.login(username='testuser', password='testpassword123')
        self.assertTrue(login)
    
    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')
    
    def test_signup_functionality(self):
        # Test user creation through the signup form
        user_count = User.objects.count()
        
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newuserpassword123',
            'password2': 'newuserpassword123',
        })
        
        # Should redirect to profile setup
        self.assertRedirects(response, reverse('profile_setup'))
        # Check that a new user was created
        self.assertEqual(User.objects.count(), user_count + 1)
    
    def test_profile_view_requires_login(self):
        # Test that profile view requires login
        response = self.client.get(reverse('profile'))
        # Should redirect to login
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('profile')}")
        
        # Now login and try again
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile.html')
    
    def test_profile_setup_view(self):
        # Test profile setup view (requires login)
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('profile_setup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/profile_setup.html')
    
    def test_profile_setup_functionality(self):
        # Test profile update functionality
        self.client.login(username='testuser', password='testpassword123')
        
        response = self.client.post(reverse('profile_setup'), {
            'learning_language': 'FR',
            'proficiency_level': 'INT',
            'chosen_field': 'MED',
        })
        
        # Should redirect to profile
        self.assertRedirects(response, reverse('profile'))
        
        # Check that profile was updated
        updated_profile = UserProfile.objects.get(user=self.test_user)
        self.assertEqual(updated_profile.learning_language, 'FR')
        self.assertEqual(updated_profile.proficiency_level, 'INT')
        self.assertEqual(updated_profile.chosen_field, 'MED')


class UserProfileModelTests(TestCase):
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        self.test_user.save()
        
        # User profile should be automatically created via signals
        self.profile = UserProfile.objects.get(user=self.test_user)
    
    def test_profile_creation(self):
        # Test that profile is created automatically
        self.assertIsNotNone(self.profile)
        
        # Test default values
        self.assertEqual(self.profile.learning_language, 'EN')
        self.assertEqual(self.profile.proficiency_level, 'BEG')
        self.assertEqual(self.profile.chosen_field, 'GEN')
    
    def test_profile_str_method(self):
        # Test the string representation of the profile
        self.assertEqual(str(self.profile), "testuser's profile")
    
    def test_profile_update(self):
        # Test updating profile
        self.profile.learning_language = 'ES'
        self.profile.proficiency_level = 'ADV'
        self.profile.chosen_field = 'MED'
        self.profile.save()
        
        # Fetch fresh from DB to verify
        updated_profile = UserProfile.objects.get(id=self.profile.id)
        self.assertEqual(updated_profile.learning_language, 'ES')
        self.assertEqual(updated_profile.proficiency_level, 'ADV')
        self.assertEqual(updated_profile.chosen_field, 'MED')