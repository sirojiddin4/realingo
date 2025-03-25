from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib import messages
from .forms import SignUpForm, UserProfileForm, UserUpdateForm, CustomPasswordChangeForm
from .models import UserProfile, Tutor

def home(request):
    """View for the home page"""
    context = {}
    if request.user.is_authenticated:
        user_profile = request.user.profile
        context['profile'] = user_profile
        
        # Get assigned tutor or default to the first available tutor
        if user_profile.assigned_tutor:
            context['tutor'] = user_profile.assigned_tutor
        else:
            # Get available tutors
            available_tutors = Tutor.objects.filter(is_active=True)
            if available_tutors.exists():
                context['tutor'] = available_tutors.first()
        
        # Get all tutors for selection modal
        context['all_tutors'] = Tutor.objects.filter(is_active=True)
    
    return render(request, 'home.html', context)

def menu(request):
    """View for the main menu page"""
    return render(request, 'menu.html')

def about(request):
    """View for the about page"""
    return render(request, 'about.html')

def signup(request):
    """View for user registration"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f"Account created for {username}. Now let's set up your learning profile!")
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

@login_required
def profile(request):
    """View for user profile page with account settings"""
    user_form = UserUpdateForm(instance=request.user)
    profile_form = UserProfileForm(instance=request.user.profile)
    password_form = CustomPasswordChangeForm(request.user)
    
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'profile':
            profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, "Your profile has been updated successfully!")
                return redirect('profile')
        
        elif form_type == 'user':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Your account information has been updated successfully!")
                return redirect('profile')
        
        elif form_type == 'password':
            password_form = CustomPasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Keep user logged in
                messages.success(request, "Your password has been updated successfully!")
                return redirect('profile')
    
    # Get all available tutors for selection
    tutors = Tutor.objects.filter(is_active=True)
    
    return render(request, 'account/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'password_form': password_form,
        'tutors': tutors
    })

@login_required
def assign_tutor(request, tutor_id):
    """View to assign a tutor to the user"""
    if request.method == 'POST':
        try:
            tutor = Tutor.objects.get(id=tutor_id, is_active=True)
            user_profile = request.user.profile
            user_profile.assigned_tutor = tutor
            user_profile.save()
           
        except Tutor.DoesNotExist:
            messages.error(request, "The selected tutor is not available.")
    
    return redirect('home')

# Keep this for backward compatibility but redirect to profile
@login_required
def profile_setup(request):
    """Redirect to profile page"""
    return redirect('profile')

@login_required
def start_learning(request):
    """View for starting a learning session"""
    # This will be expanded later with actual learning content
    return render(request, 'learning/start.html')

def about(request):
    """View for the about page"""
    return render(request, 'about.html')