from django.contrib import admin
from django.urls import path

from schedule.views import *

urlpatterns = [
    path('campus/<int:pk>', CampusUDView.as_view()),
    path('campus/', CampusCRView.as_view()),
    path('lessons/<int:pk>', LessonUDView.as_view()),
    path('lessons/', LessonCRView.as_view()),
    path('rings/<int:pk>', RingTimeUDView.as_view()),
    path('rings/', RingTimeCRView.as_view()),
    path('tutor/<int:pk>', TutorUDView.as_view()),
    path('tutor/', TutorCRView.as_view()),
    path('auditorium/<int:pk>', AuditoriumUDView.as_view()),
    path('auditorium/', AuditoriumCRView.as_view()),
    path('group/<int:pk>', GroupUDView.as_view()),
    path('group/', GroupCRView.as_view()),
]
