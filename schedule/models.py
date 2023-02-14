from django.db import models


# Create your models here.
class Campus(models.Model):
    address = models.CharField(max_length=128)
    short = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = "Корпуса"
        verbose_name = "Корпус"

    def __str__(self):
        return self.short.__str__()


# class Subject(models.Model):
#     name = models.CharField(max_length=32)
#
#     def __str__(self):
#         return self.name


class Tutor(models.Model):
    # Require
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    # Nullable
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Преподаватели"
        verbose_name = "Преподаватель"

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.patronymic


class RingTime(models.Model):
    # Require
    number = models.SmallIntegerField(verbose_name="Номер")
    special = models.CharField(max_length=64, verbose_name="Пояснение", help_text="Добавьте пояснение к особому расписанию звонком, допустим: \" Праздничное, пары по 1 часу \"", null=True, blank=True)
    begin = models.TimeField(verbose_name="Начало")
    end = models.TimeField(verbose_name="Конец")
    corp = models.ForeignKey("Campus", on_delete=models.CASCADE, verbose_name="Корпус")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = "Расписание звонков"
        verbose_name = "Расписание звонков"

    def __str__(self):
        return "Расписание звонков " + self.corp.short.__str__()


class Auditorium(models.Model):
    # Require
    short = models.CharField(max_length=8)
    number = models.CharField(max_length=8)
    corp = models.ForeignKey("Campus", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Аудитории"
        verbose_name = "Аудитория"

    def __str__(self):
        return self.short.__str__() + " " + self.corp.short.__str__()


class Lesson(models.Model):
    # Require

    ring_time = models.ForeignKey("RingTime", on_delete=models.CASCADE, verbose_name="Номер")
    date = models.DateField(verbose_name="Дата")
    subject = models.CharField(max_length=48, verbose_name="Предмет")
    tutor = models.ForeignKey("Tutor", on_delete=models.CASCADE, verbose_name="Преподаватель")
    group = models.ForeignKey("Group", on_delete=models.CASCADE, verbose_name="Группа")
    subgroup = models.SmallIntegerField(null=True, blank=True, verbose_name="Подгруппа", help_text="При необходимости разбейте группу на подгруппы")
    auditorium = models.ForeignKey("Auditorium", on_delete=models.CASCADE, verbose_name="Аудитория")



    def __str__(self):
        return self.date + " Группа " + self.group.name.__str__() + " " + "#" + self.ring_time.number.__str__()

    class Meta:
        unique_together = [['date', 'ring_time', 'tutor'],
                           ['date', 'ring_time', 'group', 'subgroup'],
                           ['tutor', 'group', 'date', 'ring_time'],
                           ['group', 'auditorium', 'date', 'ring_time'],
                           ['ring_time', 'group', 'date'],
                           ['ring_time', 'tutor', 'date'],
                           ['tutor', 'group', 'auditorium', 'ring_time', 'date']]

        verbose_name_plural = "Расписание"
        verbose_name = "Занятие"


class Group(models.Model):
    # Require
    name = models.CharField(max_length=16)
    allow_subgroup = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Группы"
        verbose_name = "Группа"

    def __str__(self):
        return self.name.__str__()

class LessonMain(models.Model):
    ring_time = models.ForeignKey("RingTime", on_delete=models.CASCADE, verbose_name="Номер")
    dayofweek = models.CharField(max_length=16, verbose_name="День недели")
    subject = models.CharField(max_length=48, verbose_name="Предмет")
    tutor = models.ForeignKey("Tutor", on_delete=models.CASCADE, verbose_name="Преподаватель")
    group = models.ForeignKey("Group", on_delete=models.CASCADE, verbose_name="Группа")
    subgroup = models.SmallIntegerField(null=True, blank=True, verbose_name="Подгруппа", help_text="При необходимости разбейте группу на подгруппы")
    auditorium = models.ForeignKey("Auditorium", on_delete=models.CASCADE, verbose_name="Аудитория")

    def __str__(self):
        return self.dayofweek + " Группа " + self.group.name.__str__() + " " + "#" + self.ring_time.number.__str__()

    class Meta:
        unique_together = [['dayofweek', 'ring_time', 'tutor'],
                           ['dayofweek', 'ring_time', 'group', 'subgroup'],
                           ['tutor', 'group', 'dayofweek', 'ring_time'],
                           ['group', 'auditorium', 'dayofweek', 'ring_time'],
                           ['ring_time', 'tutor', 'dayofweek'],
                           ['tutor', 'group', 'auditorium', 'ring_time', 'dayofweek']]

        verbose_name_plural = "Основное расписание"
        verbose_name = "Занятие"