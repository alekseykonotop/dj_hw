from django.views.generic import ListView

from .models import Student


class StudentListView(ListView):
    template_name = 'school/student_list.html'
    model = Student
    ordering = 'group'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
