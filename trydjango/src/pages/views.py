from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
#	return HttpResponse("<h1>It works!</h1>")
	return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
	# print(args,kwargs)
	# print(request.user)
	#return HttpResponse("<br><br>About page is up and running")

	my_context = {
		"my_text": "This is about me",
		"my_number": 44562,
		"my_list" : [25, 56, 74],
		"my_html" : "<p> this is html paragrapgh </p>",
	}
	return render (request, "about.html", my_context)

def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {});

