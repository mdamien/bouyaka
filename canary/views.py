from django.shortcuts import get_object_or_404, render, render_to_response, redirect

def tell(request,name,line):
	name = name.replace('_',' ').title()
	line = line.replace('_',' ')
	return render(request, 'canary/tell.html', {'name':name,'line':line})

def shorttell(request,line):
	return tell(request,"Damien",line)

def index(request):
	return tell(request,"Damien","a raison")