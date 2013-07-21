from django.shortcuts import get_object_or_404, render, render_to_response, redirect
import string

def rot13(s):
	rot13 = string.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
		"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
	return string.translate(s, rot13)

def tell(request,line):
	line = line.replace("_"," ")
	return render(request, 'canary/tell.html', {'line':line})

def index(request):
	return tell(request,"Welcome")

def r13(request,line):
	return tell(request,line.encode("rot13"))