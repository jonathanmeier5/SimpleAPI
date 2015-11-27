from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import Friend
from .forms import FriendForm

# Create your views here.
def base(request):
    return HttpResponse("This is the base of the API! :)")

def get_friends(request,friend_count):
    
    friends = {}
    school_friends = {1:'mary',2:'jane'}
    football_friends = {1:'chris',2:'bob',3:'billbob'}
    friends['group1']=school_friends
    friends['group2']=football_friends
    return JsonResponse(data=friends,safe=False)
    
def add_friends(request):
    
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your friend was added!")
    else:
        return HttpResponse("There was an error, your friend was not added")
    
    
    
