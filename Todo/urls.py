

from django.urls import path,include


from .import views

urlpatterns = [
    path('',views.task_new, name='task_new'),
    path('task_list',views.task_list, name='task_list'),
    path('Task/<int:pk>/delete/',views.task_delete,name='task_delete'),
    path('Task/<int:pk>/update/',views.task_update, name='task_update'),
    
    
]
