from django.shortcuts import render, get_object_or_404
from .models import Member

# Create your views here.
def all_members(request):
  members= Member.objects.all()
  return render(request, 'team/all_members.html', {'members': members})

def member_detail(request, member_id):
  member= get_object_or_404(Member, pk= member_id)
  return render(request, 'team/member_detail.html', {'member': member})