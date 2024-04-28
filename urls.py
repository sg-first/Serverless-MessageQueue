from django.urls import path
from . import views

urlpatterns = [
    path('pop/', views.queuePop),
    path('insert/', views.queueInsert),
]
