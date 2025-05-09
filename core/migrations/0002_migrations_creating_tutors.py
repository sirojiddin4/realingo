# Generated by Django 4.2.7
from django.db import migrations, models
import django.db.models.deletion
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.models.tutor_image_path)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('specialty', models.CharField(choices=[('GEN', 'General Conversation'), ('BUS', 'Business Language'), ('MED', 'Medical Terminology'), ('ACA', 'Academic Language'), ('TRA', 'Travel & Tourism'), ('LIT', 'Literature & Arts'), ('TEC', 'Technical & Engineering')], default='GEN', max_length=3)),
                ('characteristics', models.TextField(help_text='Short background and teaching style of the tutor')),
                ('years_experience', models.PositiveIntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.user_profile_image_path),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='assigned_tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='core.tutor'),
        ),
    ]