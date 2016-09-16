from django import forms

class AddForm(forms.form):
	"""docstring for AddForm"""
	a = forms.IntergerField()
	b = forms.IntergerField()