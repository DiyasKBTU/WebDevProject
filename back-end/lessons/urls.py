from django.urls import path
from .views import get_lessons, create_lesson

urlpatterns = [
    path('<int:course_id>/', get_lessons),             # /api/lessons/1/
    path('<int:course_id>/create/', create_lesson),    # /api/lessons/1/create/
]
