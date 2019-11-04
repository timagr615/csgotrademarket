from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login_view(request):
	name1 = 'wqdf gdfvsdawee rewfe'
	return render(request, 'authentication/authPage.html', {'name': name1})


@login_required
def logout_view(request):
	auth_logout(request)
	return redirect('auth:authPage')
