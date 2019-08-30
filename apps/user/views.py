from django.shortcuts import render, redirect, HttpResponse
from .models import User
import bcrypt
from django.contrib import messages


def index(request):
    return render(request, 'user/index.html')

def dashboard(request):
    if 'id' not in request.session:
        return redirect('/')

    
    return render(request, 'user/dashboard.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            context = {
                'message' : errors
            }

            print(context['message'])
            return render(request, 'user/index.html', context)

        else:
            pwordhash = bcrypt.hashpw(request.POST['Password'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name=request.POST['FirstName'], last_name=request.POST['LastName'], displayname=request.POST['DisplayName'], email=request.POST['Email'].lower(), password=pwordhash)
            request.session['id'] = user.id
            request.session['displayname'] = user.displayname
            request.session['firstname'] = user.first_name
            request.session['lastname'] = user.last_name
            print(request.session['id'])

            return redirect('/dashboard')

def login(request):
    print('$' * 40)
    print(request.POST['LoginEmail'].lower())
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)
        
        
        if len(errors) >0:
            context = {
                'message' : errors
            }

            print(context['message'])
            return render(request, 'user/index.html', context)
        else:
            user = User.objects.get(email=request.POST['LoginEmail'].lower())
            request.session['id'] = user.id
            request.session['displayname'] = user.displayname
            request.session['firstname'] = user.first_name
            request.session['lastname'] = user.last_name
            return redirect('/dashboard')

def logout(request):
    del request.session['id']
    del request.session['displayname']
    del request.session['firstname']
    del request.session['lastname']
    return redirect('/')

