from django import forms
from blog.models import Post,Man
from django import forms
from django.db import models
from django.forms import ModelForm


class Man(forms.ModelForm):
	class Meta:
		model=Man
		fields = ['id','name','age']