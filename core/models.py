from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
import os

def user_profile_image_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/user_<id>/profile/<filename>
    return f'user_{instance.user.id}/profile/{filename}'

def tutor_image_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/tutors/<tutor_id>/<filename>
    return f'tutors/{instance.id}/{filename}'

class UserProfile(models.Model):
    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('FR', 'French'),
        ('ES', 'Spanish'),
        ('DE', 'German'),
        # Add more languages as needed
    ]
    
    PROFICIENCY_LEVELS = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('ADV', 'Advanced'),
    ]
    
    FIELD_CHOICES = [
        ('GEN', 'General'),
        ('MED', 'Medical'),
        # Add more fields as needed
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to=user_profile_image_path, null=True, blank=True)
    learning_language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    proficiency_level = models.CharField(max_length=3, choices=PROFICIENCY_LEVELS, default='BEG')
    chosen_field = models.CharField(max_length=3, choices=FIELD_CHOICES, default='GEN')
    assigned_tutor = models.ForeignKey('Tutor', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
    def profile_image_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url
        return None

class Tutor(models.Model):
    SPECIALTY_CHOICES = [
        ('GEN', 'General Conversation'),
        ('BUS', 'Business Language'),
        ('MED', 'Medical Terminology'),
        ('ACA', 'Academic Language'),
        ('TRA', 'Travel & Tourism'),
        ('LIT', 'Literature & Arts'),
        ('TEC', 'Technical & Engineering'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=tutor_image_path, null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(5)])
    specialty = models.CharField(max_length=3, choices=SPECIALTY_CHOICES, default='GEN')
    characteristics = models.TextField(help_text="Short background and teaching style of the tutor")
    years_experience = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return None

# Signal to create user profile automatically when a user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()