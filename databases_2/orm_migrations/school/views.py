from django.views.generic import ListView

from .models import Student


class StudentListView(ListView):
    template_name = 'school/student_list.html'
    model = Student
    ordering = 'group'

    def get_context_data(self):
        students = Student.objects.all().prefetch_related('teachers')
        context = {
            'students': students,
        }

        return context
