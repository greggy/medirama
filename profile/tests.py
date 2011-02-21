from django.test.client import Client
from django.test import TestCase

from models import *


class PersonTest(TestCase):
    fixtures = ['data.json']
    
    def setUp(self):
        self.profession = Profession.objects.create(title='medical doctor')
        self.specialty = Specialty.objects.create(title='Cardiologie')
        self.c = Client()
        
    def test_post_creation(self):
        response = self.c.post('/profile/add/', {'first_name': u'Greg', 'last_name': u'Johns', 
                                                'certificate': u'0', 'confirm_email': u'gfborn@gmail.com', 
                                                'profession': self.profession.id, 'specialty': self.specialty.id, 
                                                'sex': u'0', 'phone': u'4012345678', 'email': u'gfborn@gmail.com'})
        self.assertEqual(response.status_code, 302)
        response = self.c.post('/profile/add/', {'first_name': u'Greg', 'last_name': u'Johns', 
                                                'certificate': u'0', 'confirm_email': u'gfborn@gmail.com', 
                                                'profession': self.profession.id, 'specialty': self.specialty.id, 
                                                'sex': u'0', 'phone': u'4012345678', 'email': u'gfborn@gmail.com'})
        #self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This email exist in db, choose another.', status_code=200)
        
    def test_get_person(self):
        response = self.c.get('/profile/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '\nTest Teter\n')


