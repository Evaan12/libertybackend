# domain/admin.py

from django.contrib import admin
from .models.about import Mission, Vision, CoreValue, Milestone
from .models.academics import CurriculumPhilosophy, CurriculumPillar, Subject, GradeLevel
# Import the new Facility model
from .models.facilities import Facility

# --- Existing About Section Admin ---
@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request):
        return not Mission.objects.exists()

@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request):
        return not Vision.objects.exists()

@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'description')
    list_filter = ('icon',)

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('year', 'event', 'description')
    ordering = ('year',)

# --- New Academics Section Admin ---

@admin.register(CurriculumPhilosophy)
class CurriculumPhilosophyAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request):
        return not CurriculumPhilosophy.objects.exists()

@admin.register(CurriculumPillar)
class CurriculumPillarAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'description')
    list_filter = ('icon',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'description')
    list_filter = ('icon',)

@admin.register(GradeLevel)
class GradeLevelAdmin(admin.ModelAdmin):
    list_display = ('level', 'focus')
    ordering = ('id',)

# --- New Facilities Section Admin ---
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'description')
    search_fields = ('title', 'description')