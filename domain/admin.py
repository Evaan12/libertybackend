from django.contrib import admin
from .models.about import Mission, Vision, CoreValue, Milestone

admin.site.register(Mission)
admin.site.register(Vision)
admin.site.register(CoreValue)
admin.site.register(Milestone)