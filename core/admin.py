from django.contrib import admin
from .models import UserProfile, Tutor

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'learning_language', 'proficiency_level', 'chosen_field', 'assigned_tutor', 'created_at')
    list_filter = ('learning_language', 'proficiency_level', 'chosen_field', 'assigned_tutor')
    search_fields = ('user__username', 'user__email')
    autocomplete_fields = ('assigned_tutor',)

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialty', 'rating', 'years_experience', 'is_active')
    list_filter = ('specialty', 'is_active')
    search_fields = ('name',)
    readonly_fields = ('created_at',)