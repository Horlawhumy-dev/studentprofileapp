from django.shortcuts import render
from account.models import StudentAccount


# Create your views here.
def index(request):
    students = StudentAccount.objects.all()
    return render(request, 'students/index.html',{'students': students})