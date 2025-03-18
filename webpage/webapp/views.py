from django.views.generic import TemplateView

# Class Based Views  (CBV)
class HomePageView(TemplateView):
    template_name='webapp/home.html'

class AboutPageView(TemplateView):
    template_name = 'webapp/about.html'

class CoursesPageView(TemplateView):
    template_name = 'webapp/courses.html'

class StudentsPageView(TemplateView):
    template_name = 'webapp/students.html'
