from django.urls import path
from .views import TaskList, TaskCreate, TaskUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns= [
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    
    # path('', RegisterPage.as_view(), name='register'),
    # path('tasks/', TaskList.as_view(), name='tasks'),
    
    path('',TaskList.as_view(),name='tasks'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
   # path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),
    
]