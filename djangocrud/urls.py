from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create', views.create_task, name='create_task'),
    path('task/<int:tax_id>/', views.task_detail, name='task'),
    path('task/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('task/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('tasks_completed', views.tasks_completed, name='tasks_completed'),
    path('logout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin')
]
