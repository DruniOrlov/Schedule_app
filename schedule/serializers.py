from rest_framework import serializers

from schedule import models


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Campus
        fields = '__all__'


class TutorSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=False)
    phone = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = models.Tutor
        fields = ["first_name", "last_name", "patronymic", "email", "phone"]


class TutorNameSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return '{} {} {}'.format(obj.first_name, obj.last_name, obj.patronymic)

    class Meta:
        model = models.Tutor
        fields = ["full_name"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class DaySerializer():
    pass

class LessonSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField()
    begin = serializers.DateTimeField()
    end = serializers.DateTimeField()
    subject = serializers.CharField(max_length=32)
    tutor = TutorNameSerializer()
    group = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )
    auditorium = serializers.SlugRelatedField(
        read_only=True,
        slug_field="short"
    )

    class Meta:
        model = models.Lesson
        fields = '__all__'


class RingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RingTime
        fields = '__all__'


class AuditoriumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Auditorium
        fields = '__all__'
