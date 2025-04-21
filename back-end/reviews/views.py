from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Review
from .serializers import ReviewSerializer
from courses.models import Course

class ReviewListView(APIView):
    def get(self, request, course_id):
        reviews = Review.objects.filter(course_id=course_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class ReviewCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        # Проверка если пользовател оставил отзыв
        if Review.objects.filter(course=course, user=request.user).exists():
            return Response({'error': 'You have already reviewed this course'}, status=400)

        data = request.data.copy()
        data['course'] = course.id
        data['user'] = request.user.id
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
