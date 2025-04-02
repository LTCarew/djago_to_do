
from django.contrib import admin
from django.urls import path
from home.views import home
from add_task.views import addTask, edit_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'homepage'),
    path('edit_task/<pk>', edit_task, name = 'edit-task'),
    path('add_new_task/',addTask,name='add-task' )
]

