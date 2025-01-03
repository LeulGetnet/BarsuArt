from django.contrib import admin
from django.contrib import admin
from .models import Artwork, ArtworkImage

class OriginalImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1

class OriginalsAdmin(admin.ModelAdmin):
    inlines = [OriginalImageInline]

admin.site.register(Artwork, OriginalsAdmin)

# Register your models here.
