from django.db import models


class PomodoroStatus(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    name = models.CharField(max_length=200)
    length_work = models.IntegerField(default=1200)
    length_break = models.IntegerField(default=300)
    length_long_break = models.IntegerField(default=900)
    long_break_after = models.IntegerField(default=4)


class PomodoroStatusLog(models.Model):
    id = models.UUIDField
    length_work = models.IntegerField(default=1200)
    length_break = models.IntegerField(default=300)
    length_long_break = models.IntegerField(default=900)
    long_break_after = models.IntegerField(default=4)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    time = models.DateTimeField("Time")
    status = models.ForeignKey(PomodoroStatus, on_delete=models.CASCADE)
