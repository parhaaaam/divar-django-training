from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Unit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.views.generic import RedirectView





# Create your views here.

class UnitList(LoginRequiredMixin, ListView) : 
    model = Unit
    template_name = 'unitlist.html'
    
    # def get_queryset(self, *args, **kwargs):
    #     qs = super(UnitList, self).get_queryset(*args, **kwargs)
    #     qs = qs.filter(user=self.request.user)
    #     return qs
 