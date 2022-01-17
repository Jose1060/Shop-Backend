from django.urls import path
from shop_api import views

urlpatterns = [
    path('hello-view/', views.HelloWorld.as_view()),
]