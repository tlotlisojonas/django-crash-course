from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Learner, Subject
from .forms import SubjectRegistrationForm, LearnerRegistrationForm
from django.contrib import messages

# Create your views here.
def index(request):
    learners = list(Learner.objects.all())
    context = {
        "learners":learners
    }
    return render(request,'student/index.html',context)


def detail(request, id):
    learner = Learner.objects.filter(id=id)[0]

    if request.method == 'POST':
        form = SubjectRegistrationForm(data=request.POST)
        if form.is_valid():
            record = form
            sel_subject = record.cleaned_data['subject']

        if Subject.objects.filter(learner=learner,subject=sel_subject).exists():
            messages.warning(request,f'You are already enrolled for this subject!')
        else:
            sb = Subject(subject=sel_subject,learner=learner)   
            sb.save()
            messages.success(request,f'Subject added successfully!') 

    else:
        form =  SubjectRegistrationForm() 

    subjects = Subject.objects.filter(learner=learner)   
    subjects = [subjects[i].subject for i in range(len(subjects))]         

    context = {
        "name":learner.name,
        "age":learner.age,
        "subjects":subjects,
        "form":form
    }
    return render(request,'student/detail.html', context)

def registration(request):
    if request.method=='POST':
        form = LearnerRegistrationForm(data=request.POST)
        if form.is_valid():
            record = form
            record.save()
            return redirect('/')
        else:
            form = LearnerRegistrationForm()
            context = {
                "form":form
            }
            messages.warning(request, f'Please make sure the data is valid!') 
            return render(request,'student/register.html',context)            
               
    else:
        form = LearnerRegistrationForm()
        context = {
            "form":form
        }
        return render(request,'student/register.html',context)

