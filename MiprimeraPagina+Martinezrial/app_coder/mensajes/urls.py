from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox_view, name='inbox'),
    path('chat/<str:username_receptor>/', views.chat_view, name='chat_view'),
    path('start/', views.start_chat_view, name='start_chat'),
]