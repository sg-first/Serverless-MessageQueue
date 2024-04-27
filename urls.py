from django.urls import path
import djangodemo.views as views

urlpatterns = [
    path('pop/', views.queuePop),
    path('insert/', views.queueInsert),
]
