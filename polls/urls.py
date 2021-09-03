from django.urls import path

from polls import views

urlpatterns = [
    # 数据备份
    path('hello/', views.hello, name='hello'),
    path('update/', views.update, name='update'),
    path('list/', views.list, name='list'),
    path('task/', views.task, name='task'),

    path('view/<str:uuid>/', views.TestView.as_view()),

]
