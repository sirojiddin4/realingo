# Realingo: Interactive Language Learning App

Realingo is an innovative language learning platform that combines AI-generated storytelling with interactive language exercises. Users learn languages through engaging mini-stories that are tailored to their proficiency level and chosen field of interest.

## Features

- **Story-Driven Learning**: Learn languages through interactive mini-stories
- **Adaptive Content**: Content adjusts to match your proficiency level
- **Field-Specific Learning**: Focus on vocabulary relevant to your chosen field (e.g., general, medical)
- **Post-Story Training**: Reinforce vocabulary with dedicated training sessions
- **Competitive Elements**: Practice with other learners in 1-on-1 role-play sessions
- **Personalized Journey**: Build a cumulative narrative of your language learning progress

## Technical Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (development) / PostgreSQL (production)
- **AI Integration**: ChatGPT API for dynamic story generation

## Getting Started

### Prerequisites

- Python 3.8+
- Django 4.2+

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/realingo.git
   cd realingo
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

```
realingo/
├── manage.py
├── realingo/            # Project settings
├── core/                # Main app
├── templates/           # HTML templates
└── static/              # Static files (CSS, JS, images)
```

## Future Enhancements

- Integration with speech recognition and synthesis
- Additional language fields beyond general and medical
- Enhanced social features like user communities and discussion forums
- Mobile application
- Gamification elements (achievements, streaks, etc.)

## License

This project is licensed under the MIT License - see the LICENSE file for details.