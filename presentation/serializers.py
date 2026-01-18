# presentation/serializers.py

from rest_framework import serializers
from domain.models.about import Mission, Vision, CoreValue, Milestone
from domain.models.academics import CurriculumPhilosophy, CurriculumPillar, Subject, GradeLevel
# Import the new Facility model
from domain.models.facilities import Facility

# --- Existing About Serializers ---
class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class VisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vision
        fields = '__all__'

class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = '__all__'

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

# --- New Academics Serializers ---
class CurriculumPhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumPhilosophy
        fields = ['title', 'description']

class CurriculumPillarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumPillar
        fields = ['title', 'description', 'icon']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'description', 'icon']

class GradeLevelSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    class Meta:
        model = GradeLevel
        fields = ['level', 'focus', 'description', 'subjects']
    def get_subjects(self, obj):
        return [subject.strip() for subject in obj.subjects_offered.split(',')]

# --- New Facilities Serializer ---
class FacilitySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Facility
        fields = ['id', 'title', 'description', 'image', 'icon']
    
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None