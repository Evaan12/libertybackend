from django.db import models

class CurriculumPhilosophy(models.Model):
    title = models.CharField(max_length=200, default="Our Curriculum Philosophy")
    description = models.TextField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Curriculum Philosophy"


class CurriculumPillar(models.Model):
    ICON_CHOICES = [
        ('BookOpen', 'Book Open'),
        ('Palette', 'Palette'),
        ('Trophy', 'Trophy'),
        ('Globe', 'Globe'),
        ('Microscope', 'Microscope'),
        ('Calculator', 'Calculator'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)

    def __str__(self):
        return self.title

class Subject(models.Model):
    ICON_CHOICES = [
        ('BookOpen', 'English / Literature'),
        ('Calculator', 'Mathematics'),
        ('Microscope', 'Sciences'),
        ('Globe', 'Social Studies'),
        ('Languages', 'Foreign Languages'),
        ('Palette', 'Arts & Crafts'),
        ('Music', 'Music & Performing Arts'),
        ('Trophy', 'Physical Education'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES)

    def __str__(self):
        return self.name
    
class GradeLevel(models.Model):
    level = models.CharField(max_length=100, help_text="e.g., Primary (Grades 1-5)")
    focus = models.CharField(max_length=100, help_text="e.g., Foundation Building")
    description = models.TextField()
    subjects_offered = models.TextField(help_text="Enter subjects separated by commas, e.g., English, Mathematics, Science")

    def __str__(self):
        return self.level