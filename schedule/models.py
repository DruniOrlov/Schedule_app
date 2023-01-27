from django.db import models


# Create your models here.
class Campus(models.Model):
    address = models.CharField(max_length=128)
    short = models.CharField(max_length=16)

    def __str__(self):
        return self.short


class Subject(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Tutor(models.Model):
    # Require
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    # Nullable
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.patronymic


class RingTime(models.Model):
    # Require
    number = models.SmallIntegerField()
    begin = models.TimeField()
    end = models.TimeField()
    corp = models.ForeignKey("Campus", on_delete=models.CASCADE)

    def __str__(self):
        return self.corp


class Auditorium(models.Model):
    # Require
    short = models.CharField(max_length=8)
    number = models.CharField(max_length=8)
    corp = models.ForeignKey("Campus", on_delete=models.CASCADE)

    def __str__(self):
        return self.short


class Lesson(models.Model):
    # Require
    number = models.SmallIntegerField()
    begin = models.DateTimeField()
    end = models.DateTimeField()
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE) #models.CharField(max_length=32)
    tutor = models.ForeignKey("Tutor", on_delete=models.CASCADE)
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
    auditorium = models.ForeignKey("Auditorium", on_delete=models.CASCADE)

    def __str__(self):
        return self.begin.date().__str__()

class Group(models.Model):
    # Require
    name = models.CharField(max_length=16)
    allow_subgroup = models.BooleanField(default=True)

    def __str__(self):
        return self.name