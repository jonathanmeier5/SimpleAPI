from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
from .models import Friend
from .forms import FriendForm

# Create your views here.
def base(request):
    return HttpResponse("This is the base of the API! :)")

def get_friends(request,firstName):
        
    if request.method=="GET":
        #data = serializers.serialize("json",Friend.objects.get(firstName=firstName))
        data = serializers.serialize('json',Friend.objects.filter(firstName=firstName))
        return JsonResponse(data=data,safe=False)
            #HttpResponse("Testing to see if this works")
        '''else:
            data = serializers.serialize("json",Friend.objects.get(name=name))
            #return HttpResponse("didn't retrieve")
            return JsonResponse(data=data,safe=False)'''
    else:
        return HttpResponse("Was not a get request!")
    
def add_friends(request):
    
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your friend was added!")
    else:
        return HttpResponse("There was an error, your friend was not added")
    
    
def delete_friends(request,firstName):
    
    if request.method == 'DELETE':
        friend = Friend.objects.get(firstName=firstName)
        friend.delete()
        return HttpResponse("Friend "+friend.firstName+" was deleted")
    else:
        return HttpResponse("The delete didn't work")

def update_friends(request,firstName):
    
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
        
            friend, created = Friend.objects.update_or_create(get(firstName=firstName,
                                                            default=form))
        if created:
            return HttpResponse("had to create a new guy")
        else:
            return HttpResponse("Updated the thing")
    else:
        return HttpResponse("You really need to use a POST")

        
    
    
    
    
    
