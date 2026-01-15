from rest_framework import serializers
from domain.models.about import Mission, Vision, CoreValue, Milestone

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