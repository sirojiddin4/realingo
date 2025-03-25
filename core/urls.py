from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('assign-tutor/<int:tutor_id>/', views.assign_tutor, name='assign_tutor'),
    # Keep this for backward compatibility
    path('profile/setup/', views.profile_setup, name='profile_setup'),
    path('start-learning/', views.start_learning, name='start_learning'),
]