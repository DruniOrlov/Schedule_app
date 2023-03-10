import http
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from schedule.models import *
from schedule.serializers import *


class CampusCRView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    serializer_class = CampusSerializer
    queryset = Campus.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CampusUDView(mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   generics.GenericAPIView):
    serializer_class = CampusSerializer
    queryset = Campus.objects.all()
    permission_classes = [IsAdminUser | IsAuthenticatedOrReadOnly]

    def get(self, request, pk, *args, **kwargs):
        try:
            data = CampusSerializer(self.queryset.get(id=pk))
            response = Response(status=http.HTTPStatus.OK, data=data.data)
        except Campus.DoesNotExist:
            data = {"message": f"Campus with id={pk} not found"}
            response = Response(status=http.HTTPStatus.NOT_FOUND, data=data)
        return response

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AuditoriumCRView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    serializer_class = AuditoriumSerializer
    queryset = Auditorium.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuditoriumUDView(mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    serializer_class = AuditoriumSerializer
    queryset = Auditorium.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request, pk, *args, **kwargs):
        try:
            data = AuditoriumSerializer(self.queryset.get(id=pk))
            response = Response(status=http.HTTPStatus.OK, data=data.data)
        except Auditorium.DoesNotExist:
            data = {"message": f"Auditorium with id={pk} not found"}
            response = Response(status=http.HTTPStatus.NOT_FOUND, data=data)
        return response

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class GroupCRView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GroupGetWithId(mixins.ListModelMixin,
                     generics.GenericAPIView):
    serializer_class = GroupWithIdSerializer
    queryset = Group.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class GroupUDView(mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request, pk, *args, **kwargs):
        try:
            data = GroupSerializer(self.queryset.get(id=pk))
            response = Response(status=http.HTTPStatus.OK, data=data.data)
        except Group.DoesNotExist:
            data = {"message": f"Group with id={pk} not found"}
            response = Response(status=http.HTTPStatus.NOT_FOUND, data=data)
        return response

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RingTimeCRView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    serializer_class = RingTimeSerializer
    queryset = RingTime.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RingTimeUDView(mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    serializer_class = RingTimeSerializer
    queryset = RingTime.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request, pk, *args, **kwargs):
        try:
            data = RingTimeSerializer(self.queryset.get(id=pk))
            response = Response(status=http.HTTPStatus.OK, data=data.data)
        except RingTime:
            data = {"message": f"Ring timetable with id={pk} not found"}
            response = Response(status=http.HTTPStatus.NOT_FOUND, data=data)
        return response

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TutorCRView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    serializer_class = TutorNameSerializer
    queryset = Tutor.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TutorGetWithId(mixins.ListModelMixin,
                     generics.GenericAPIView):

    serializer_class = TutorNameIdSerializer
    queryset = Tutor.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class TutorUDView(mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    serializer_class = TutorNameSerializer
    queryset = Tutor.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request, pk, *args, **kwargs):
        try:
            data = TutorNameSerializer(self.queryset.get(id=pk))
            response = Response(status=http.HTTPStatus.OK, data=data.data)
        except Tutor.DoesNotExist:
            data = {"message": f"Tutor with id={pk} not found"}
            response = Response(status=http.HTTPStatus.NOT_FOUND, data=data)
        return response

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DayScheduleView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    lesson_queryset = Lesson.objects.all()

    def get(self, request, *args, **kwargs):
        if request.GET.get("date") is None:
            return Response(status=http.HTTPStatus.BAD_REQUEST, data={"message": "param date require"})
        date = datetime.strptime(request.GET.get("date"), "%d.%m.%Y")
        lessons = self.lesson_queryset.filter(date=date.date())
        if request.GET.get("group") is None and request.GET.get("tutor") is None:
            return Response(status=http.HTTPStatus.BAD_REQUEST, data={"message": "param group or tutor require"})
        if request.GET.get("group"):
            if lessons.filter(group_id=int(request.GET.get("group"))):
                lessons = lessons.filter(group_id=int(request.GET.get("group"))).order_by('ring_time__number')
            else: lessons = None
        elif request.GET.get("tutor"):
            if lessons.filter(tutor_id=int(request.GET.get("tutor"))):
                lessons = lessons.filter(tutor_id=int(request.GET.get("tutor"))).order_by('ring_time__number')
            else: lessons = None
        serialized = {"date": date,
                      "lessons": LessonSerializer(lessons, many=True).data}
        if serialized:
            return Response(status=http.HTTPStatus.OK, data=serialized)
        return Response(status=http.HTTPStatus.INTERNAL_SERVER_ERROR, data={"error": "internal server error"})


class LessonCRView(generics.GenericAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        response = self.queryset
        if request.GET.get("date"):
            date = datetime.strptime(request.GET.get("date"), "%d.%m.%Y")
            response = response.filter(begin__year=date.year, begin__month=date.month, begin__day=date.day)
        if request.GET.get("tutor"):
            response = response.filter(tutor_id=request.GET.get("tutor"))
        if request.GET.get("group"):
            group = request.GET.get("group")
            response = response.filter(group__name=group)

        return Response(status=http.HTTPStatus.OK, data=LessonSerializer(response, many=True).data)

    def post(self, request, *args, **kwargs):
        lesson = None
        return None


class LessonUDView(mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request, pk, *args, **kwargs):
        try:
            data = LessonSerializer(self.queryset.get(id=pk))
            response = Response(status=http.HTTPStatus.OK, data=data.data)
        except Lesson.DoesNotExist:
            data = {"message": f"Lesson with id={pk} not found"}
            response = Response(status=http.HTTPStatus.NOT_FOUND, data=data)
        return response

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def index(request):
    context = {}
    return render(request, "index.html", context)