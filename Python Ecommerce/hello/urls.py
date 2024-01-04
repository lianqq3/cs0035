from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path('post/', views.individual_post, name='individual_post')
]