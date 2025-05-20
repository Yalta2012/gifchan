from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, SignupForm, ChangeForm
from django.contrib.auth import update_session_auth_hash

def signup_view(request):
	if (request.method == 'POST'):
		form = SignupForm(request.POST)
		if (form.is_valid()):
			user = form.save()
			login(request,user)
			return redirect('homepage')
	else:
		form = SignupForm()
	return render(request, 'signup.html',{'form':form})

def login_view(request):
	if(request.method == 'POST'):
		form = LoginForm(data=request.POST)
		if (form.is_valid()):
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST['next'])
			return redirect('homepage')
	else:
		form = LoginForm()
	return render(request, 'login.html',{'form':form})

@login_required(login_url='accounts:login')
def change_view(request):
	if(request.method == 'POST'):
		form = ChangeForm(user=request.user, data=request.POST or None)
		if(form.is_valid()):
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('homepage')
	else:
		form = ChangeForm(user = request.user)
	return render(request,'change.html',{'form':form})

def logout_view(request):
	if (request.method == 'POST'):
		logout(request)
	return redirect(request.path)