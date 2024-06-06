from django.shortcuts import render
from subTeacher.forms import SigninForm,LoginForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from subTeacher.models import STsignin,STLogIn
from data.models import Student
from django.contrib.auth import authenticate, login
from django.shortcuts import render
import json




# Create your views here.
def homepage(request):
    return render(request,'index.html')
def stSignin(request):
    form1=SigninForm
    dict1={'form1':form1}
    if request.method=='POST':
        form1=SigninForm(request.POST)
        if form1.is_valid():
            mail=form1.cleaned_data['mail']
            password3 = form1.cleaned_data['password']
            password4= form1.cleaned_data['password1']
            if STsignin.objects.filter(mail=mail).exists():
                return HttpResponse("Email already exists.Please click on log in to continue")
            if password3==password4:
                form1.save()
                return HttpResponse("Sign in succesful")

    return render(request,'subTeacher/signin.html',dict1)
def login(request):
    form2 = LoginForm()
    dict2 = {'form2': form2}
    if request.method == 'POST':
        form2 = LoginForm(request.POST)
        if form2.is_valid():
            mail1 = form2.cleaned_data['user_mail']
            password3 = form2.cleaned_data['user_password']
            user_exists = STsignin.objects.filter(mail=mail1).exists()

            if user_exists:
                user = STsignin.objects.get(mail=mail1)
                if user.password == password3:
                    return marksManage(request)
                else:
                    return HttpResponse("Incorrect Password")
            else:
                return HttpResponse("User does not exist. Please sign up.")

    return render(request, 'subTeacher/login.html', dict2)

# views.py


def marksManage(request):
    if request.method == 'POST':
        course = request.POST.get('course', '')
        sub = request.POST.get('sub', '')
        print("Course:", course)
        print("Sub:", sub)
        
        if course == "AI&DS-3rd year":
            students = Student.objects.filter(branch="AI&DS")
            ds = {"students": students, "sub": sub}
            return render(request, 'subTeacher/marks.html', ds)

        # Handle form submission
        if 'marks_submit' in request.POST:
            sub = request.POST.get('sub', '')
            marks = request.POST.getlist('marks')

            # Update the data_student table with subject marks
            for student, mark in zip(Student.objects.all(), marks):
                student.subject_marks = mark
                student.save()

    return render(request, 'subTeacher/marks.html')
