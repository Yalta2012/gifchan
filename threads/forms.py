from django import forms
from . import models

class ThreadForm(forms.ModelForm):
	class Meta:
		model = models.Thread
		fields=['title','text','image']
		labels={
			"title":"Title",
			"text":"Text",
			"image":"Image"
		}
		widgets ={
			"title" : forms.TextInput(attrs={'placeholder' : 'Write article title', 'class' : 'form-control mb-3'}),
			"text" : forms.TextInput(attrs={'placeholder' : 'Write article text', 'class' : 'form-control mb-3'}),
			"image" : forms.ClearableFileInput(attrs={'class' : 'form-control mb-3'})
		}

class MessageForm(forms.ModelForm):
	class Meta:
		model = models.Message
		fields = ['text','image']
		labels={
			"text":"Text",
			"image":"Image"
		}