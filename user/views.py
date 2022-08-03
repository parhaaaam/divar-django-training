from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate  , login 


class Index (TemplateView) : 

    template_name = 'index.html'

class Log_in(TemplateView) : 

    template_name = 'login.html'
    error = None

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if self.error:
            context['error'] = self.error
        return context

    def post (request) : 

        username = request.POST['username']
        password = request.POST['password'] 
        current_user = authenticate(request , username = username , password = password)

        if current_user is not None : 

            login(request , current_user) 
        
        else :
            return self.get()


class register() : 

    pass