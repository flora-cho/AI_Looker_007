from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListtblAdvtBsc.as_view()),
    path('<int:pk>/', views.DetailtblAdvtBsc.as_view()),
]