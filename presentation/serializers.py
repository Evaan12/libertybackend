from rest_framework import serializers
from domain.models.about import Mission, Vision, CoreValue, Milestone
# Import the new academics models
from domain.models.academics import CurriculumPhilosophy, CurriculumPillar, Subject, GradeLevel

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
    # Create a custom field to split the comma-separated subjects into a list
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = GradeLevel
        fields = ['level', 'focus', 'description', 'subjects']

    def get_subjects(self, obj):
        # Split the string by comma and strip whitespace from each subject
        return [subject.strip() for subject in obj.subjects_offered.split(',')]