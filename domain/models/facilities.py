# domain/models/facilities.py

from django.db import models

class Facility(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # This setting is correct. It will place uploaded files inside
    # a 'facilities_images' subfolder within your main media directory.
    image = models.ImageField(upload_to='facilities_images/')
    icon = models.CharField(max_length=50, help_text="Enter a lucide-react icon name (e.g., Library, Microscope)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Facilities"