from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models.about import Mission, Vision, CoreValue, Milestone
# Import new academics models
from .models.academics import CurriculumPhilosophy, CurriculumPillar, Subject, GradeLevel

def invalidate_about_page_cache(sender, **kwargs):
    cache.delete('about_page_data')
    print("\n\n>>>>>>>>>> SIGNAL FIRED! Cache has been invalidated for 'about_page_data' <<<<<<<<<<\n\n")

# New function for academics cache
def invalidate_academics_page_cache(sender, **kwargs):
    cache.delete('academics_page_data')
    print("\n\n>>>>>>>>>> SIGNAL FIRED! Cache has been invalidated for 'academics_page_data' <<<<<<<<<<\n\n")

# Connect signals for About page
models_to_watch_about = [Mission, Vision, CoreValue, Milestone]
for model in models_to_watch_about:
    post_save.connect(invalidate_about_page_cache, sender=model)
    post_delete.connect(invalidate_about_page_cache, sender=model)

# Connect signals for Academics page
models_to_watch_academics = [CurriculumPhilosophy, CurriculumPillar, Subject, GradeLevel]
for model in models_to_watch_academics:
    post_save.connect(invalidate_academics_page_cache, sender=model)
    post_delete.connect(invalidate_academics_page_cache, sender=model)