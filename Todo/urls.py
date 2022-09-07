

from django.urls import path,include


from .import views

urlpatterns = [
    path('',views.task_new, name='task_new'),
    # path('',views.task_list,  name='task_list'),
    # path('',views.task_new, name='task_new'),
    path('task_list',views.task_list, name='task_list'),
    # path('task/new/',views.task_new, name='task_new'),
    path('Task/<int:pk>/delete/',views.task_delete,name='task_delete'),
    # path('Task/<int:pk>/update/',views.task_update,name='task_update'),
    # path('task_update',views.task_update,name='task_update'),
    path('Task/<int:pk>/update/',views.task_update, name='task_update'),
    
    
]
