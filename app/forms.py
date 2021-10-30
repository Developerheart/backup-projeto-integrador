from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class UsuarioForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		usuario = super(UsuarioForm, self).save(commit=False)
		usuario.email = self.cleaned_data['email']
		if commit:
			usuario.save()
		return usuario