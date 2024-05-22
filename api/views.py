from django.shortcuts import render
from rest_framework import generics

from api.models import BlogPost
from api.serializers import BlogPostSerializer


class BlogPostListCreate(generics.ListCreateAPIView):
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer
	