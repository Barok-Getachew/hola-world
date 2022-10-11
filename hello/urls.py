from django.urls import path
from hello import views 

urlpatterns = [
    path('all/', views.todo)
]