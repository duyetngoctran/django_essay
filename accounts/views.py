from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Essay, Student


def register(request):
  if request.method == 'POST':
   
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create_user(username=username, password=password,email=email)
          # Login after register
          # auth.login(request, user)
          # messages.success(request, 'You are now logged in')
          # return redirect('index')
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
    #   messages.success(request, 'You are now logged in')
      return redirect('home')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def logout(request):
  if request.method == 'POST':
    print("test")
    auth.logout(request)
    # messages.success(request, 'You are now logged out')
    return redirect('login')

@login_required
def dashboard(request):
    student = get_object_or_404(Student, user=request.user)
    essays = Essay.objects.order_by('-created').filter(student=student)

    context = {
      'essays': essays
    }
    return render(request, 'accounts/dashboard.html', context)


def essay_detail(request, essay_id):
    essay = get_object_or_404(Essay, pk=essay_id)

    context = {
      'essay': essay
    }

    return render(request, 'accounts/essay.html', context)