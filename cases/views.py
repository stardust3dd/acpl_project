from django.shortcuts import render, get_object_or_404
from .models import Case

# Create your views here.
def all_cases(request):
  cases= Case.objects.all()
  return render(request, 'cases/all_cases.html', {'cases': cases})

def case_detail(request, case_id):
  case= get_object_or_404(Case, pk= case_id)
  return render(request, 'cases/case_details.html', {'case': case})