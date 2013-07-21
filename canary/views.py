from django.shortcuts import get_object_or_404, render, render_to_response, redirect

def tell(request,name,line):
	name = name.title()
	line = line.replace('_',' ')
	return render(request, 'canary/tell.html', {'name':name,'line':line})