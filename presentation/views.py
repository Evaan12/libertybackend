from rest_framework.views import APIView
from rest_framework.response import Response
from infrastructure.repositories.about_repository import AboutRepository
from .serializers import MissionSerializer, VisionSerializer, CoreValueSerializer, MilestoneSerializer

class AboutPageAPIView(APIView):
    def get(self, request, *args, **kwargs):
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
        return Response(response_data)