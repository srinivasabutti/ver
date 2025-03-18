from django.urls import path

from .views import HomePageView
from .views import AboutPageView
from .views import CoursesPageView
from .views import StudentsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('courses/', CoursesPageView.as_view(), name='courses'),
    path('students/', StudentsPageView.as_view(), name='students'),
    path('', HomePageView.as_view(), name='home'),
]
