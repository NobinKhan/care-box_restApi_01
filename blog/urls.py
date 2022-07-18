from django.urls import path
from blog import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.Blogs.as_view()),
    path('<int:pk>/', views.Blogs.as_view()),
]


# urlpatterns = format_suffix_patterns(urlpatterns)