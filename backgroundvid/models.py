from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
# models.py
from django.db import models
from django.core.exceptions import ValidationError

from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

class Video(models.Model):
    video = CloudinaryField(
        'video', 
        resource_type='video',  # Explicitly specify video
        allowed_formats=['mp4', 'mov', 'avi', 'mkv', 'webm']  # Add allowed video formats
    )

    def clean(self):
        """
        Ensure only one video object exists and the file is valid.
        """
        if Video.objects.exists() and not self.pk:
            raise ValidationError("Only one video can be uploaded.")

        # Check file extension (for additional validation, optional)
        if not self.video.name.lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.webm')):
            raise ValidationError("Invalid video file format. Please upload a valid video.")

    def save(self, *args, **kwargs):
        self.clean()  # Validate before saving
        super().save(*args, **kwargs)

    
