from django.utils.timezone import make_aware, get_current_timezone
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta


# Create your views here.
class Blogs(APIView):
    def getDate(self, data):
        new_datetime = datetime.strptime(data, '%Y-%m-%d')
        timzone_datetime = make_aware(new_datetime)
        return timzone_datetime

    def get(self, request, pk=None, format=None):
        if request.query_params.get('endDate') and request.query_params.get('startDate'):
            endDate = self.getDate(request.query_params.get('endDate'))
            startDate = self.getDate(request.query_params.get('startDate'))
            blogs = Blog.objects.filter(created_at__range=[startDate, endDate+timedelta(days=1)])
            serializer = BlogSerializer(blogs, many=True, context={'request': request})
            return Response(serializer.data)
        
        if pk:
            blog = get_object_or_404(Blog, pk=pk)
            serializer = BlogSerializer(blog, context={'request': request})
            return Response(serializer.data)
        blogs = Blog.objects.all().order_by('created_at')
        serializer = BlogSerializer(blogs, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog = get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response({'message':"Successfully Deleted"},status=status.HTTP_204_NO_CONTENT)

