"""
Script to initialize sample tutors in the database.
Run this after migrations are complete:
    python load_tutors.py
"""

import os
import django
import decimal

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realingo.settings')
django.setup()

# Import models
from core.models import Tutor

# Sample tutors data
TUTORS = [
    {
        'name': 'Sarah Johnson',
        'rating': decimal.Decimal('4.9'),
        'specialty': 'GEN',
        'years_experience': 8,
        'characteristics': 'Sarah is a friendly and patient tutor who specializes in conversational skills. '
                          'With a background in linguistics, she can help you understand the nuances of language '
                          'and develop natural fluency. She believes in learning through real-world examples.'
    },
    {
        'name': 'David Chen',
        'rating': decimal.Decimal('4.7'),
        'specialty': 'BUS',
        'years_experience': 12,
        'characteristics': 'David is an experienced business language coach who has worked with executives '
                          'from multinational companies. He focuses on professional vocabulary, presentations, '
                          'and business etiquette. His teaching style is direct and results-oriented.'
    },
    {
        'name': 'Maria Rodriguez',
        'rating': decimal.Decimal('4.8'),
        'specialty': 'MED',
        'years_experience': 10,
        'characteristics': 'Maria is a former medical professional who now specializes in teaching medical '
                          'terminology and healthcare communication. She uses case studies and role-playing '
                          'to prepare students for real clinical scenarios. Her approach is methodical and thorough.'
    },
    {
        'name': 'James Wilson',
        'rating': decimal.Decimal('4.5'),
        'specialty': 'ACA',
        'years_experience': 7,
        'characteristics': 'James specializes in academic language, helping students with research papers, '
                          'presentations, and scholarly discussions. He has a PhD in Education and believes '
                          'in a structured approach to learning with clear milestones and regular assessments.'
    },
    {
        'name': 'Emma Thompson',
        'rating': decimal.Decimal('4.6'),
        'specialty': 'TRA',
        'years_experience': 5,
        'characteristics': 'Emma is a travel enthusiast and language expert who focuses on practical travel vocabulary '
                          'and cultural etiquette. Her classes are fun, interactive, and full of real-life scenarios '
                          'you might encounter while traveling. She believes in immersive learning experiences.'
    },
    {
        'name': 'Michael Okafor',
        'rating': decimal.Decimal('4.9'),
        'specialty': 'LIT',
        'years_experience': 15,
        'characteristics': 'Michael is a published author who specializes in teaching language through literature and arts. '
                          'He helps students develop sophisticated vocabulary and expression through analyzing and '
                          'creating literary works. His teaching style is creative, reflective, and deeply engaging.'
    },
]

def create_tutors():
    """Create sample tutors in the database"""
    for tutor_data in TUTORS:
        tutor, created = Tutor.objects.get_or_create(
            name=tutor_data['name'],
            defaults={
                'rating': tutor_data['rating'],
                'specialty': tutor_data['specialty'],
                'years_experience': tutor_data['years_experience'],
                'characteristics': tutor_data['characteristics'],
                'is_active': True
            }
        )
        
        if created:
            print(f"Created tutor: {tutor.name}")
        else:
            print(f"Tutor already exists: {tutor.name}")

if __name__ == '__main__':
    print("Creating sample tutors...")
    create_tutors()
    print("Done!")