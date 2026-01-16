# presentation/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from infrastructure.repositories.about_repository import AboutRepository
from .serializers import MissionSerializer, VisionSerializer, CoreValueSerializer, MilestoneSerializer
import time # Import time for a timestamp

class AboutPageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cache_key = 'about_page_data'
        
        print(f"\n[{time.ctime()}] --- VIEW HIT: Attempting to get cache for key: '{cache_key}' ---")
        
        # 1. Try to get data from cache first
        cached_data = cache.get(cache_key)
        
        if cached_data:
            print(f"[{time.ctime()}] >>> CACHE HIT! Returning cached data.")
            return Response(cached_data)

        # 2. If not in cache, fetch from DB
        print(f"[{time.ctime()}] --- CACHE MISS! Fetching data from database... ---")
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

        # 3. Store the response data in the cache
        print(f"[{time.ctime()}] <<< Storing new data in cache. Timeout: 7200 seconds.")
        cache.set(cache_key, response_data, timeout=7200)

        return Response(response_data)