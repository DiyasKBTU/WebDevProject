from django.urls import path
from .views import ReviewListView, ReviewCreateView

urlpatterns = [
    path('<int:course_id>/', ReviewListView.as_view()),         # GET /api/reviews/1/
    path('<int:course_id>/create/', ReviewCreateView.as_view()) # POST /api/reviews/1/create/
]
