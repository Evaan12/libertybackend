# domain/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models.about import Mission, Vision, CoreValue, Milestone

def invalidate_about_page_cache(sender, **kwargs):
    cache.delete('about_page_data')
    print("\n\n>>>>>>>>>> SIGNAL FIRED! Cache has been invalidated for 'about_page_data' <<<<<<<<<<\n\n")

models_to_watch = [Mission, Vision, CoreValue, Milestone]
for model in models_to_watch:
    post_save.connect(invalidate_about_page_cache, sender=model)
    post_delete.connect(invalidate_about_page_cache, sender=model)