from django.shortcuts import render, redirect, HttpResponse
from .models import Comment, Reply
from ..user.models import User
from django.contrib import messages
def list(request):
    if 'id' not in request.session:
        return redirect('/')
    return render(request, 'forums/list.html')

def forum(request, event_id):
    if 'id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    comments = Comment.objects.filter(eventId = event_id)
    context = {
        'Comments' : comments,
        'EventId' : event_id,
        'user' : user
    }
    print(request.session['id'])
    return render (request, 'forums/forum.html', context) 

def postComment(request):
    if request.method == "POST":
        print(request.POST['comment'])
        eventId = request.POST['eventId']
        errors = Comment.objects.comment_validator(request.POST)
        if len(errors) > 0:
            return redirect(f'/forums/{eventId}')
        
        else:
            Commenter = User.objects.get(id= request.POST['userId'])
            New_Comment = Comment.objects.create(content=request.POST['comment'], commenter=Commenter, eventId=eventId)
            return redirect(f'/forums/{eventId}')


            # commenter = User.objects.get(id=request.POST['userId'])

        