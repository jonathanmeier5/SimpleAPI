from django.test import TestCase, Client
from django.core import serializers
from .models import Friend
import json

def add_friend():
    
    friend3 = {'firstName':"Bob",
                    'lastName':"Billy"}
    Friend.objects.create(**friend3)


class FriendsTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        friend1 = {'firstName':"john",
                        'lastName':"bane"}
        friend2 = {'firstName':'Becky',
                    'lastName':'Barns',
                    'phone':'18601234567'}
        self.friend1 = Friend.objects.create(**friend1)
        self.friend2 = Friend.objects.create(**friend2)
        
    def test_add_friend(self):

        friend3 = {'firstName':"Bob",
                        'lastName':"Billy"}
        friend4 = {'firstName':"Brett",
                    'lastName':'Hemmingway'}
                    
        response = self.client.post('/api/friends/add/', friend3)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Friend.objects.count(),3)
        
        response = self.client.post('/api/friends/add/', friend4)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Friend.objects.count(),4)
        
    def test_get_friend(self):
        
        response = self.client.get('/api/friends/get/john/')
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(json.loads(response.content.decode()),
                                serializers.serialize("json",Friend.objects.filter(firstName="john")))
        
        add_friend()
        
        response = self.client.get('/api/friends/get/Becky/')
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(json.loads(response.content.decode()),
                                serializers.serialize("json",Friend.objects.filter(firstName="Becky")))
        
    def test_delete_friend(self):
        
        self.assertEqual(Friend.objects.count(),2)
        
        response = self.client.delete('/api/friends/delete/john/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Friend.objects.count(),1)
        
        