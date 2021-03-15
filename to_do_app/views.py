from django.shortcuts import render
from drf_spectacular.contrib.django_filters import DjangoFilterBackend
from rest_framework import mixins, status
from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
)
from rest_framework.response import Response

from .serializers import TaskCreateSerializer, TaskListSerializer, \
    TaskCompletedSerializer, TaskRetrievSerializer, TaskUpdateStatusOrderSerializer
from .models import Task


class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskRetrievView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskRetrievSerializer


class TaskNotCompletedListView(ListAPIView):
    queryset = Task.objects.filter(completed=False)
    serializer_class = TaskListSerializer


class TaskCompletedListView(ListAPIView):
    queryset = Task.objects.filter(completed=True)
    serializer_class = TaskCompletedSerializer


class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskRetrievSerializer
    http_method_names = ['put']


class TaskUpdateStatusView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateStatusOrderSerializer
    lookup_field = 'title'
    http_method_names = ['patch']


class CompletedDestroyView(mixins.DestroyModelMixin,
                     GenericAPIView):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TaskCompletedDeleteView(CompletedDestroyView):
    queryset = Task.objects.filter(completed=True)
    serializer_class = TaskCompletedSerializer
    lookup_field = 'completed'
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['completed']


# class TaskOneView(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskRetrievSerializer
#


# Create your views here.
