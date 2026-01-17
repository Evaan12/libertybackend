# presentation/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from infrastructure.repositories.about_repository import AboutRepository
# Import new academics repository and serializers
from infrastructure.repositories.academics_repository import AcademicsRepository
from .serializers import (
    MissionSerializer, VisionSerializer, CoreValueSerializer, MilestoneSerializer,
    CurriculumPhilosophySerializer, CurriculumPillarSerializer, SubjectSerializer, GradeLevelSerializer
)
import time

# --- Existing About Page API View ---
class AboutPageAPIView(APIView):
    # ... (no changes here) ...
    def get(self, request, *args, **kwargs):
        cache_key = 'about_page_data'
        
        cached_data = cache.get(cache_key)
        
        if cached_data:
            print(f"[{time.ctime()}] CACHE HIT! Returning cached data for About Page.")
            return Response(cached_data)

        print(f"[{time.ctime()}] --- CACHE MISS! Fetching About Page data from database... ---")
        repository = AboutRepository()
        
        mission = repository.get_mission()
        vision = repository.get_vision()
        core_values = repository.get_all_core_values()
        milestones = repository.get_all_milestones()

        mission_data = MissionSerializer(mission).data if mission else {}
        vision_data = VisionSerializer(vision).data if vision else {}
        core_values_data = CoreValueSerializer(core_values, many=True).data
        milestones_data = MilestoneSerializer(milestones, many=True).data

        response_data = {
            'mission': mission_data,
            'vision': vision_data,
            'values': core_values_data,
            'milestones': milestones_data,
        }

        print(f"[{time.ctime()}] <<< Storing new About Page data in cache. Timeout: 7200 seconds.")
        cache.set(cache_key, response_data, timeout=7200)

        return Response(response_data)


# --- New Academics Page API View ---
class AcademicsPageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cache_key = 'academics_page_data'
        
        cached_data = cache.get(cache_key)
        if cached_data:
            print(f"[{time.ctime()}] CACHE HIT! Returning cached data for Academics Page.")
            return Response(cached_data)
        
        print(f"[{time.ctime()}] --- CACHE MISS! Fetching Academics Page data from database... ---")
        repository = AcademicsRepository()

        philosophy = repository.get_philosophy()
        pillars = repository.get_all_pillars()
        subjects = repository.get_all_subjects()
        grade_levels = repository.get_all_grade_levels()

        response_data = {
            'philosophy': CurriculumPhilosophySerializer(philosophy).data if philosophy else {},
            'pillars': CurriculumPillarSerializer(pillars, many=True).data,
            'subjects': SubjectSerializer(subjects, many=True).data,
            'grade_levels': GradeLevelSerializer(grade_levels, many=True).data
        }

        print(f"[{time.ctime()}] <<< Storing new Academics Page data in cache. Timeout: 7200 seconds.")
        cache.set(cache_key, response_data, timeout=7200)

        return Response(response_data)