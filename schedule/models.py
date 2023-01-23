from django.db import models


# Create your models here.
class Campus(models.Model):
    #id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=128)
    short = models.CharField(max_length=16)


class Tutor(models.Model):
    # Require
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    # Nullable
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10)


class RingTime(models.Model):
    # Require
    number = models.SmallIntegerField()
    begin = models.TimeField()
    end = models.TimeField()
    corp = models.ForeignKey("Campus", on_delete=models.CASCADE)


class Auditorium(models.Model):
    # Require
    short = models.CharField(max_length=8)
    number = models.CharField(max_length=8)
    corp = models.ForeignKey("Campus", on_delete=models.CASCADE)


class Lesson(models.Model):
    # Require
    number = models.SmallIntegerField()
    begin = models.DateTimeField()
    end = models.DateTimeField()
    subject = models.CharField(max_length=32)
    tutor = models.ForeignKey("Tutor", on_delete=models.CASCADE)
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
    auditorium = models.ForeignKey("Auditorium", on_delete=models.CASCADE)


class Group(models.Model):
    # Require
    name = models.CharField(max_length=16)
    allow_subgroup = models.BooleanField(default=True)
