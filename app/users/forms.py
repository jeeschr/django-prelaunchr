from .models import User
from django import forms

class ContestForm(forms.ModelForm):
	email = forms.EmailField(error_messages={'required': 'Let us know where to reach you', 
										'invalid':'Enter an email address like abc@xyz.com',
										'unique':'That email address has already signed up'})
	class Meta:
		model = User
		fields = ['email']
		# exclude = ['referral_code','referrer']