from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteTask, LogIn,SingIn
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LogIn.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('singin/',SingIn.as_view(),name='singin'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),  # se cauta de pe id
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
]
