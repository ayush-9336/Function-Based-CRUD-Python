from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)  #Here fm is object
        if fm.is_valid():                         #use to save data
            nm= fm.cleaned_data['name']  #fm if form that access data which we enter in textfield. nm is just a variable
            em= fm.cleaned_data['email']                #em is just a variable
            pw= fm.cleaned_data['password']                #pw is just a variable
            reg= User(name=nm, email=em, password=pw)  #reg is object of User class
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()          #for all data include
    return render(request,'enroll/addandshow.html', {'form':fm,'stu':stud})

#this function is for update(edit)
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})

#this function is for delete 
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)   #to get only one data
        pi.delete()
        return HttpResponseRedirect('/')