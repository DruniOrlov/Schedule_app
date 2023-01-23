from rest_framework import serializers

from schedule import models


class CampusSerializer(serializers.ModelSerializer):

    #id = serializers.IntegerField(required=False)

    class Meta:
        model = models.Campus
        fields = '__all__'
        #read_only_fields = ['id']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tutor
        fields = '__all__'


class RingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RingTime
        fields = '__all__'


class AuditoriumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Auditorium
        fields = '__all__'

