from django.urls import path
from . import views

urlpatterns = [
	# path('', views.index, name='index'),
	path('blogpost/', views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
	path('blogpost/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-update'),
]