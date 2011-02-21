# -*- coding: utf-8 -*-
import uuid

from django.template import RequestContext 
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from forms import PersonForm
from models import Person


def get_profile(request, person_id):
    'Get person info.'
    person = get_object_or_404(Person, id=person_id)
    
    return render_to_response('person.html', {'person': person}, context_instance=RequestContext(request))
    
    
def add_profile(request):
    'Add user profile.'
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #un = str(uuid.uuid4()).split('-')[0]
            #new_user = User.objects.create(username=un, email=cd['email'], first_name=cd['first_name'], 
            #                               last_name=cd['last_name'], password='111')
            new_person = form.save(commit=False)
            #new_person.user = new_user
            new_person.save()
            return HttpResponseRedirect(reverse('get-profile', args=[new_person.id]))
        #else:
        #    print form.errors['email']
    else:
        context = {'phone': '40xxxxxxxxx'}
        form = PersonForm(initial=context)
    
    return render_to_response('profile.html', {'form': form}, context_instance=RequestContext(request))
