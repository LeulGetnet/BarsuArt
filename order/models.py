from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
class OrderFormDescription(models.Model):
      title = models.CharField(max_length=70)
      description = models.TextField()
      created_at = models.DateTimeField(auto_now=True)

      def __str__(self):
            return str(self.created_at)
class Order(models.Model):
    user_name = models.CharField(max_length=255)
    description = models.TextField()
    #sample_photo = models.ImageField(upload_to='sample_photos/')
    sample_photo = CloudinaryField('image')
    wanted_size = models.CharField(max_length=20)
    style = models.CharField(choices=[('detailed', 'Detailed'), ('abstract', 'Abstract')], max_length=50)
    email_or_phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # # def validate_contact_info(phone_number, email):
    # #     if not phone_number and not email:
    # #         raise ValidationError('At least one of phone number or email must be provided.')
    # def clean(self):
    #         self.validate_contact_info(self.phone_number, self.email)

    def __str__(self):
            return self.user_name

