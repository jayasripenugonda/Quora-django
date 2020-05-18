from django.shortcuts import render


def homepage(request):
	return render(request, "Pages/homepage.html")

def register(request):
	return render(request, "Pages/register.html")

def login(request):
	return render(request, "Pages/login.html")

def profile(request):
	return render(request, "Pages/profile.html")		

def updateprofile(request):
	return render(request, "Pages/update_profile.html")

def about(request):
	return render(request, "Pages/about.html")

def askquestion(request):
	return render(request, "Pages/ask_question.html")

def answerquestion(request):
	return render(request, "Pages/Answer.html")
# Create your views here.
