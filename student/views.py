from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .serializers import StudentSerializer, AddressSerializer
from .models import Student, Address
from rest_framework.response import Response

class StudentAPIView(APIView):
    def get(self, request, *args, **kwargs):
        standard = request.GET.get('standard')
        student_name = request.GET.get('student_name')
        students = Student.objects.all()
        if student_name:
            students = Student.objects.filter(student_name=student_name)
        if standard:
            students = students.filter(standard=standard) 
        student_serializer = StudentSerializer(students, many=True)
        if student_serializer.data:
            return Response(student_serializer.data)
        else:
            return Response({'msg':'No data found'})

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



