from django.contrib import admin
from .models import *
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_display = ['ring_time', 'date', 'group', 'tutor']
    list_filter = ['ring_time', 'group', 'tutor']


class LessonMainAdmin(admin.ModelAdmin):
    list_display = ['ring_time', 'dayofweek', 'group', 'tutor']
    list_filter = ['ring_time', 'group', 'tutor']


admin.site.register(Campus)
#admin.site.register(Subject)
admin.site.register(LessonMain, LessonMainAdmin)
admin.site.register(Tutor)
admin.site.register(Auditorium)
admin.site.register(RingTime)
admin.site.register(Group)
admin.site.register(Lesson, LessonAdmin)

admin.site.site_header = 'ГБПОУ КНТ им Б.И.Корнилова'
admin.site.site_title = 'Расписание'