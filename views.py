from django.shortcuts import render
from rest_framework.views import APIView
from .models import student_feedback
from .serializers import student_feedbackSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
import json

class StudentRequest(APIView):

    def get(self, request, student_id, course_id):
        student_feedback1 =student_feedback.objects.filter(student_id = student_id, course_id = course_id)
        serializer=student_feedbackSerializer(student_feedback1, many=True)
        return Response(serializer.data)

class CommentRequest(APIView):   
    def post(self, request, format = None):
        data = request.data
        data['datetime'] = datetime.now()
        feed_serializer = student_feedbackSerializer(data = data)
        if feed_serializer.is_valid():
            student_id = data['student_id']
            course_id = data['course_id']
            current = student_feedback.objects.filter(student_id = student_id, course_id = course_id)
            if current.exists():
                student_feedback.objects.filter(student_id = student_id, course_id = course_id).delete()
                        
            feed_serializer.save()
            return Response(feed_serializer.data, status=status.HTTP_201_CREATED)

        return Response(feed_serializer.data, status=status.HTTP_400_BAD_REQUEST)
            
