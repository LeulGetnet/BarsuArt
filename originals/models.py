from django.db import models
from cloudinary.models import CloudinaryField

class Artwork(models.Model):
    title = models.CharField("enter your title here: ", max_length=50)
    description = models.TextField("describe here detail info about the original", null=True, blank=True)
    category = models.CharField(choices=[('original', 'Original')], max_length=50, default='original')
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class ArtworkImage(models.Model):
    Artwork = models.ForeignKey(Artwork, related_name='images', on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='originals/photos', null=False, blank=False)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Image for {self.Artwork.title}"