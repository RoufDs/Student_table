from django.views.generic import ListView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    model: Student
    
    def get_queryset(self):
        return Student.objects.order_by('id')