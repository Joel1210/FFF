from django.shortcuts import render, redirect, HttpResponse
from .models import User
import bcrypt
from django.contrib import messages


def index(request):
    return render(request, 'user/index.html')


def dashboard(request):
    if 'id' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user,
    }
    return render(request, 'user/dashboard.html', context)


def register(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            context = {
                'message': errors
            }

            print(context['message'])
            return render(request, 'user/index.html', context)

        else:
            pwordhash = bcrypt.hashpw(
                request.POST['Password'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name=request.POST['FirstName'], last_name=request.POST['LastName'], displayname=request.POST['DisplayName'].replace(" ", ""), email=request.POST['Email'].lower(), password=pwordhash)
            request.session['id'] = user.id
            request.session['displayname'] = user.displayname
            request.session['firstname'] = user.first_name
            request.session['lastname'] = user.last_name
            request.session['email'] = user.email
            return redirect('/dashboard')


def login(request):
    print('$' * 40)
    print(request.POST['LoginEmail'].lower())
    if request.method == "POST":
        errors = User.objects.validate_login(request.POST)

        if len(errors) > 0:
            context = {
                'message': errors
            }

            print(context['message'])
            return render(request, 'user/index.html', context)
        else:
            user = User.objects.get(email=request.POST['LoginEmail'].lower())
            request.session['id'] = user.id
            request.session['displayname'] = user.displayname
            request.session['firstname'] = user.first_name
            request.session['lastname'] = user.last_name
            request.session['email'] = user.email
            return redirect('/dashboard')


def logout(request):
    del request.session['id']
    del request.session['displayname']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['email']
    return redirect('/')


def settings(request):
    if 'id' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['id'])
    context = {
        'user': user,
        'showDN': False,
        'showPW': False,
        'showEmail': False,
        'showLastName': False

    }
    return render(request, 'user/settings.html', context)


def editDN(request):
    if request.method == "POST":
        errors = User.objects.validate_displayChange(request.POST)
        print("$" * 30)
        print(errors)
        if len(errors) > 0:
            context = {
                'message': errors,
                'showDN': True
            }
            return render(request, 'user/settings.html', context)
        else:
            user = User.objects.get(id=request.session['id'])
            user.displayname = request.POST['DisplayName'].replace(" ", "")
            user.save()
            request.session['displayname'] = user.displayname

            return redirect('/settings')


def editPW(request):
    if request.method == "POST":
        errors = User.objects.validate_pwChange(request.POST)
        if len(errors) > 0:
            context = {
                'message': errors,
                'showPW': True
            }
            return render(request, 'user/settings.html', context)
        else:
            user = User.objects.get(id=request.session['id'])
            pwordhash = bcrypt.hashpw(
                request.POST['Password'].encode(), bcrypt.gensalt())
            user.password = pwordhash
            user.save()

            return redirect('/settings')


def editEmail(request):
    if request.method == "POST":
        errors = User.objects.validate_email(request.POST)
        if len(errors) > 0:
            context = {
                'message': errors,
                'showEmail': True
            }
            return render(request, 'user/settings.html', context)
        else:
            user = User.objects.get(id=request.session['id'])
            user.email = request.POST['Email']
            user.save()
            request.session['email'] = user.email

            return redirect('/settings')

def editLastName(request):
    if request.method == "POST":
        errors = User.objects.validate_lastName(request.POST)
        if len(errors) > 0:
            context = {
                'message': errors,
                'showLastName' : True
            }
            return render(request, 'user/settings.html', context)

        else:
            user = User.objects.get(id=request.session['id'])
            user.last_name = request.POST['LastName']
            user.save()
            request.session['lastname'] = user.last_name

            return redirect('/settings')

def editFirstName(request):
    if request.method == "POST":
        errors = User.objects.validate_firstName(request.POST)
        if len(errors) > 0:
            context = {
                'message': errors,
                'showFirstName' : True
            }
            return render(request, 'user/settings.html', context)

        else:
            user = User.objects.get(id=request.session['id'])
            user.first_name = request.POST['FirstName']
            user.save()
            request.session['firstname'] = user.first_name

            return redirect('/settings')