from django.urls import path
from . import views
from .views import home_view

urlpatterns = [
    path("todos/",views.todos,name="Todos"),
    path("", views.home_view, name='homeview'),
    path('receive-input/', views.receive_input, name='receive_input'),
    path('callback/', views.oauth_callback, name='oauth_callback'),
    path('submit/', views.submit_customer_info, name='submit_customer_info'),
] 