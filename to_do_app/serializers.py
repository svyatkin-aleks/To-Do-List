from rest_framework import serializers
from .models import Task


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('pk', 'title', 'description', 'deadline')


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('pk', 'title', 'description', 'deadline', 'created', 'updated', 'completed')


class TaskRetrievSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class TaskCompletedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('pk', 'title', 'description', 'deadline', 'created', 'updated', 'completed', 'order')


class TaskUpdateStatusOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('pk', 'completed', 'order')