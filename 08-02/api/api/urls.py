from django.urls import path,include

urlpatterns = [
    path('', include('task.urls')),
]
