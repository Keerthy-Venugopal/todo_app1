from django.urls import path
from.import views

urlpatterns=[
    path("",views.task_view,name='task_view'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:updateid>/',views.update,name='update'),
    path('contask/',views.TaskListview.as_view(),name='contask'),
    path('condetail/<int:pk>/',views.TaskDetailview.as_view(),name='condetail'),
    path('conupdate/<int:pk>/',views.Taskupdateview.as_view(),name='conupdate'),
    #path('condelete/<int:pk>/',views.Taskdeletevieweview.as_view(),name='condelete')
]