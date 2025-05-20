from django.shortcuts import render, redirect
from threads.models import Thread, Board, Message
from . import models,forms
from django.http import Http404
from django.contrib.auth.decorators import login_required


def board(request,slug):
	try:
		board =  Board.objects.get(slug=slug)
		threads = Thread.objects.filter(board=board).order_by("date").reverse()
	except:
		raise Http404()
	return render(request,'board.html',{"board" : board, "threads" : threads})
	
def thread(request,slug,id):
	try:
		thread = Thread.objects.get(id=id)
		messages = Message.objects.filter(thread=thread).order_by("date")
		real_slug = thread.board.slug
		if(real_slug != slug):
			return redirect('threads:thread',slug=real_slug,id = id)
	except:
		raise Http404()
	hiden_form = forms.MessageForm()
	return render(request,'thread.html',{"thread": thread, "messages":messages, 'hiden_form':hiden_form})
	# thread = Thread.objects.get(id=id)
	# messages = Message.objects.filter(thread=thread).order_by("date")
	# real_slug = thread.board.slug
	# if(real_slug != slug):
	# 	return redirect('threads:thread',slug=real_slug,id = id)
	# return render(request,'thread.html',{"thread": thread, "messages":messages})

@login_required(login_url='accounts:login')
def create_thread(request,slug):
	if(request.method=='POST'):
		form = forms.ThreadForm(request.POST, request.FILES)
		if(form.is_valid()):
			instance = form.save(commit=False)
			instance.author = request.user
			instance.board = Board.objects.get(slug=slug)
			instance.save()
			return redirect('threads:thread',slug=slug,id = instance.id)
	else:
		form=forms.ThreadForm()
	return render(request,'thread_form.html',{'form':form})

@login_required(login_url='accounts:login')
def create_message(request,slug,id,message_id=0):
	if(request.method=='POST'):
		form = forms.MessageForm(request.POST,request.FILES)
		if(form.is_valid()):
			instance = form.save(commit=False)
			instance.author = request.user
			instance.thread = Thread.objects.get(id=id)
			if(message_id!=0):
				instance.prev_message=Message.objects.get(id=message_id)
			instance.save()
			return redirect('threads:thread',slug=slug,id = id)
	else:
		form=forms.MessageForm()
	return render(request,'message_form.html',{'form':form})