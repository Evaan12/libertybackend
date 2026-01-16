from django.contrib import admin
from .models.about import Mission, Vision, CoreValue, Milestone

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