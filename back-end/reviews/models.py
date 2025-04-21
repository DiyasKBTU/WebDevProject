from django.db import models
from courses.models import Course
from users.models import CustomUser

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['course', 'user']  # Один отзыв на курс от одного пользователя

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.rating})"
