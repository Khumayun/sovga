from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def contacts_view(request, *args, **kwargs):
	contact_form=ContactForm(request.POST or None)
	context={
		'title':"Contact",
		'form':contact_form
	}
	
	if request.method=='POST':
		print(request.POST)
	return render(request, "contact/contact.html", context)