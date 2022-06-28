from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('delete/<TODOS_id>', views.delete, name='delete'),
    path('yes_finish/<TODOS_id>', views.yes_finish, name='yes_finish'),
    path('no_finish/<TODOS_id>', views.no_finish, name='no_finish'),
    path('update/<TODOS_id>', views.update, name='update'),
]
