from django.urls import path
from .views import *

app_name = 'to_do_app'

urlpatterns = [
    path('task/create', TaskCreateView.as_view()),
    path('task/list', TaskListView.as_view()),
    path('task/<str:pk>', TaskRetrievView.as_view()),
    path('task/completed/not', TaskNotCompletedListView.as_view()),
    path('task/completed/yes', TaskCompletedListView.as_view()),
    path('task/update/<str:pk>', TaskUpdateView.as_view()),
    path('task/to_complete/<path:title>', TaskUpdateStatusView.as_view()),
    # path('task/one/<str:pk>', TaskOneView.as_view())
    path('task/completed/del/<path:completed>', TaskCompletedDeleteView.as_view())
]