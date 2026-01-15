from django.db import models

class Mission(models.Model):
    title = models.CharField(max_length=100, default="Our Mission")
    description = models.TextField()

    def __str__(self):
        return self.title

class Vision(models.Model):
    title = models.CharField(max_length=100, default="Our Vision")
    description = models.TextField()

    def __str__(self):
        return self.title

class CoreValue(models.Model):
    ICON_CHOICES = (
        ("Award", "Award"),
        ("Heart", "Integrity"),
        ("Users", "Collaboration"),
        ("Target", "Innovation"),
    )
    icon = models.CharField(max_length=20, choices=ICON_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Milestone(models.Model):
    year = models.CharField(max_length=4)
    event = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['year']

    def __str__(self):
        return f"{self.year} - {self.event}"