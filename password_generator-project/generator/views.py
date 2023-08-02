from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
	return render(request, 'generator/home.html')

def about(request):
	return render(request, 'generator/about.html')

def password(request):
	characters = list('qwertyuiopasdfghjklzxcvbnm')

	if request.GET.get('uppercase'):
		characters += list('qwertyuiopasdfghjklzxcvbnm'.upper())

	if request.GET.get('special'):
		characters += list('!@#$%^&*')

	if request.GET.get('numbers'):
		characters += list('0123456789')

	lenght = int(request.GET.get('lenght', 10))

	thepassword = ''

	for x in range(lenght):
		thepassword += random.choice(characters)

	return render(request, 'generator/password.html', {"password": thepassword})