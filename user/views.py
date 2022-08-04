from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate  , login 
from django.views.generic.edit import FormView, CreateView , UpdateView
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import forms



class Index (TemplateView) : 

    template_name = 'index.html'

class Log_in(TemplateView) : 

    template_name = 'login.html'
    error = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.error:
            context['error'] = self.error
        return context

    def post (self, request) : 

        username = request.POST['username']
        password = request.POST['password'] 
        current_user = authenticate(request , username = username , password = password)

        if current_user is not None : 

            login(request , current_user) 
        
            return redirect("/user")
        else :
            self.error = "Invalid Username/password"
            return self.get(request)


class Register(CreateView) : 
    form_class = forms.NewUserForm
    template_name = 'register.html'
    success_url = '/user'

    def form_valid(self, form):
        resp = super().form_valid(form)
        user = self.object
        print(user)
        user = authenticate(self.request, username=user.username, password=form.cleaned_data.get('password1'))
        login(self.request, user)
        return resp
    
    
class Profile(TemplateView) : 

    template_name = 'profile.html'

class Update(UpdateView) : 

    model = User
    fileds = ['first_name ' , 'last_name']
    templlate_name = 'update.html'
