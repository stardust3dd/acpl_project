from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'acpl/home.html')

def contact(request):
  return render(request, 'acpl/contact.html')

def about(request):
  return render(request, 'acpl/about.html')

def digital_markeing(request):
  return render(request, 'acpl/digital_marketing.html')

def research_analytics(request):
  return render(request, 'acpl/research_analytics.html')

def marketing_solutions(request):
  return render(request, 'acpl/marketing_solutions.html')