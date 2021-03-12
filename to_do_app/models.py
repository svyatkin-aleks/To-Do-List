from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    deadline = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False, null=True, blank=True)

    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'

    ORDER = [
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVE, '5')

    ]
    order = models.CharField(choices=ORDER, default=ONE, max_length=30)

    class Meta:
        ordering = ('-deadline',)

    def __str__(self):
        return self.title


# Create your models here.
