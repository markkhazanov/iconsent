from django import forms
from .models import Join

class EmailForm(forms.Form):
	email = forms.EmailField(required=False)

class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ["email"]