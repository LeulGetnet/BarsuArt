from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class AboutMe(models.Model):
    Title = models.CharField(max_length=200, null=False, blank=False)
    ParagraphOne = models.TextField()
    ParagraphTwo = models.TextField()
    #Photo = models.ImageField(("your photo"), upload_to='about_image', height_field=None, width_field=None, max_length=None)
    Photo = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title