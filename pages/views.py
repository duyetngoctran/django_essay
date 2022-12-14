from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import requests
from accounts.models import Essay
from accounts.models import Student
from django.contrib import messages
from django.core.mail import send_mail

@login_required
def home(request):
  
    if request.method == "POST":
            
        title = request.POST.get("content")
        email = request.POST.get("email")
        user_id = request.POST.get("user_id")
        student = get_object_or_404(Student, user=request.user)
        essay = Essay.objects.create(student=student, title=title)
        
            
        if not title:
            messages.error(request, 'This field is required and cannot be empty')
            return redirect('home')
        if student.credit < 1:
            messages.error(request, 'You need more credits')
            return redirect('home')
            
                                 
        messages.success(request, 'Your request has been submitted, we will get back to you soon')
        student.credit = student.credit - 1
        
    return render(request, 'pages/home.html')


