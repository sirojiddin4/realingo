// Main JavaScript for Realingo app
document.addEventListener('DOMContentLoaded', function() {
    // 1) Handle alerts auto-close
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const closeButton = alert.querySelector('.btn-close');
            if (closeButton) {
                closeButton.click();
            }
        }, 5000); // Auto close after 5 seconds
    });

    // 2) Password visibility toggle
    const passwordFields = document.querySelectorAll('input[type="password"]');
    passwordFields.forEach(field => {
        // Create toggle button
        const toggleButton = document.createElement('button');
        toggleButton.type = 'button';
        toggleButton.className = 'btn btn-outline-secondary';
        toggleButton.innerHTML = '<i class="bi bi-eye"></i>';
        toggleButton.title = 'Show/Hide Password';

        // Wrap field in a new input group if not already
        if (!field.parentElement.classList.contains('input-group')) {
            const wrapper = document.createElement('div');
            wrapper.className = 'input-group';
            field.parentNode.insertBefore(wrapper, field);
            wrapper.appendChild(field);
        }

        // Add toggle button to input group
        field.parentElement.appendChild(toggleButton);

        // Toggle logic
        toggleButton.addEventListener('click', function() {
            if (field.type === 'password') {
                field.type = 'text';
                toggleButton.innerHTML = '<i class="bi bi-eye-slash"></i>';
            } else {
                field.type = 'password';
                toggleButton.innerHTML = '<i class="bi bi-eye"></i>';
            }
        });
    });

    // 3) Form validation enhancement
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        const submitButton = form.querySelector('button[type="submit"]');
        if (submitButton) {
            form.addEventListener('submit', function(event) {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                } else {
                    // Show loading state on button
                    submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processing...';
                    submitButton.disabled = true;
                }
                form.classList.add('was-validated');
            }, false);
        }
    });

    // 4) Tutor Selection Functionality (front-end highlight + form action)
    const tutorOptions = document.querySelectorAll('.tutor-option');
    const assignTutorForm = document.getElementById('assign-tutor-form');
    let selectedTutorId = null;

    tutorOptions.forEach(option => {
        option.addEventListener('click', function() {
            // Remove highlight from all
            tutorOptions.forEach(opt => opt.classList.remove('bg-light', 'border', 'border-primary'));

            // Highlight the clicked
            this.classList.add('bg-light', 'border', 'border-primary');

            // Store the selected tutor ID
            selectedTutorId = this.dataset.tutorId;

            // Update the form action if needed
            if (assignTutorForm) {
                assignTutorForm.action = `/assign-tutor/${selectedTutorId}/`;
            }
        });
    });

    // 5) Hover effect for navbar dropdowns on desktop
    if (window.innerWidth >= 992) {
        const dropdowns = document.querySelectorAll('.navbar .dropdown');
        dropdowns.forEach(dropdown => {
            dropdown.addEventListener('mouseover', function() {
                const dropdownMenu = this.querySelector('.dropdown-menu');
                if (dropdownMenu) {
                    dropdownMenu.classList.add('show');
                    this.querySelector('.dropdown-toggle').setAttribute('aria-expanded', 'true');
                }
            });

            dropdown.addEventListener('mouseout', function() {
                const dropdownMenu = this.querySelector('.dropdown-menu');
                if (dropdownMenu) {
                    dropdownMenu.classList.remove('show');
                    this.querySelector('.dropdown-toggle').setAttribute('aria-expanded', 'false');
                }
            });
        });
    }

    // 6) Profile image preview (user's own profile)
    const profileImageInput = document.getElementById('id_profile_image');
    if (profileImageInput) {
        profileImageInput.addEventListener('change', function() {
            if (this.files && this.files[0]) {
                const reader = new FileReader();
                const profileContainer = document.querySelector('.profile-image-container');

                reader.onload = function(e) {
                    // Check if there's already an <img>
                    let profileImg = profileContainer.querySelector('img');
                    if (!profileImg) {
                        // Remove any letter/avatar placeholder
                        const letterAvatar = profileContainer.querySelector('div.rounded-circle');
                        if (letterAvatar) {
                            letterAvatar.remove();
                        }
                        // Create new <img> for profile
                        profileImg = document.createElement('img');
                        profileImg.classList.add('rounded-circle');
                        // Enlarge to 200×200 here:
                        profileImg.style.width = '200px';
                        profileImg.style.height = '200px';
                        profileImg.style.objectFit = 'cover';
                        profileImg.style.border = '3px solid #4361ee';
                        profileContainer.appendChild(profileImg);
                    }
                    profileImg.src = e.target.result;
                    profileImg.alt = 'Profile Preview';
                };

                reader.readAsDataURL(this.files[0]);
            }
        });
    }
});
