from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Lesson
from .serializers import LessonSerializer
from courses.models import Course

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_lessons(request, course_id):
    lessons = Lesson.objects.filter(course_id=course_id)
    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_lesson(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    if course.author != request.user:
        return Response({"error": "You are not the author of this course"}, status=status.HTTP_403_FORBIDDEN)

    data = request.data.copy()
    data['course'] = course.id
    serializer = LessonSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
