from django.urls import path
from . import views
from .views import home_view

urlpatterns = [
    path("todos/",views.todos,name="Todos"),
    path("", views.home_view, name='homeview'),
    path('receive-input/', views.receive_input, name='receive_input'),
] 