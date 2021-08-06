from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import StudentAccount

# Create your views here.
def account_view(request):
    form = StudentForm()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        
        user = StudentAccount(name=name, email=email, phone=phone)
        user.save()
        return redirect('/')
    else:
     return render(request, 'account/form.html', {'form': form})


def delete(request, pk):
    student = StudentAccount.objects.get(id=pk)
    student.delete()
    return redirect('/')