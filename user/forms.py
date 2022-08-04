from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.

class NewUserForm(UserCreationForm):
    
	email = forms.EmailField(required=True)
    # first_name = forms.CharField(required = True )
    # last_name = forms.CharField(required = True )

	class Meta:
		model = User
		fields = ("first_name" , "last_name" , "username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class UpdateProfileForm(forms.ModelForm):
    
    first_naeme = forms.CharField(max_length = 256)
    last_name = forms.CharField(max_length = 256)

    class Meta:
        model = User
        fields = ['first_name', 'last_name']