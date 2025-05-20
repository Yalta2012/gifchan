from django.http import HttpResponse
from django.shortcuts import render
from threads.models import Board

def homepage(request):
	boards = Board.objects.all().order_by('title')
	return render(request,'homepage.html',{"boards": boards})

def handling404(request,exception):
	return render(request, '404.html',{})