from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
# models.py
from django.db import models
from django.core.exceptions import ValidationError

class Video(models.Model):
    #video = models.FileField(upload_to='backgroundvid/')
    video = CloudinaryField('video')

    # def clean(self):
    #     """
    #     Ensure only one video object exists in the database.
    #     """
    #     if Video.objects.exists() and not self.pk:
    #         raise ValidationError("Only one video can be uploaded.")
    def is_video_format(self):
        """
        Ensure the uploaded file is a video format.
        """
        if not self.video.name.endswith(('.mp4', '.mov', '.avi', '.mkv', '.webm')):
            raise ValidationError("Invalid video file format. Please upload a valid video.")
    
    def save(self, *args, **kwargs):
        """
        Only allow saving if no existing video objects are in the database.
        """
        if Video.objects.exists() and not self.pk:
            raise ValidationError("Only one video can be uploaded.")
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Allow deletion of the video object.
        """
        super().delete(*args, **kwargs)

    
