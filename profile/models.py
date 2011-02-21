from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Profession(models.Model):
    title = models.CharField(_('Profession'), max_length=60, blank=True)
    
    def __unicode__(self):
    	return self.title
    

class Specialty(models.Model):
    title = models.CharField(_('Medical specialty'), max_length=60, blank=True)

    def __unicode__(self):
	    return self.title
    

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female')
)

CERT_CHOICES = (
    (0, 'not asked yet'),
    (1, 'asked'),
    (2, 'already obtained')
)



class Person(models.Model):    
    first_name = models.CharField(_('First'), max_length=40)
    last_name = models.CharField(_('Last'), max_length=40)
    email =  models.CharField(_('Email'), max_length=40, unique=True)
    sex = models.IntegerField(_('Sex'), blank=True, null=True, choices=GENDER_CHOICES)
    profession = models.ForeignKey(Profession, null=True)
    specialty =  models.ForeignKey(Specialty, null=True)
    certificate = models.IntegerField(_('Certificate'), blank=True, null=True, choices=CERT_CHOICES) 
    phone = models.CharField(_('Phone number'), max_length=20)

    def __unicode__(self):
	    return "%s %s" % (self.first_name, self.last_name)
	
	
class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    person = models.ForeignKey(Person)
    
    def __unicode__(self):
    	return "%s" % (self.user,)
