import datetime

from schedule.models import LessonMain, Lesson

weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", ]


def fill_next_week():
    """
    Заполняет следующую неделю расписанием из основного
    Задачу следует запускать по субботам
    """
    main_schedule = LessonMain.objects.all()

    next_mon = datetime.date.today() + datetime.timedelta(days=(8 - datetime.date.today().isoweekday()))

    for i in range(0, 6):
        main_schedule = main_schedule.filter(dayofweek=weekdays[i])
        for record in main_schedule:
            new_record = Lesson(ring_time=record.ring_time,
                                date=next_mon + datetime.timedelta(days=i),
                                subject=record.subject,
                                tutor=record.tutor,
                                group=record.group,
                                subgroup=record.subgroup,
                                auditorium=record.auditorium)
            new_record.save()
