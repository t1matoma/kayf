from django.shortcuts import render, redirect
from .models import Art
from .forms import ArtForm
# Create your views here.
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
	news = Art.objects.order_by('-date')
	return render(request,'news/newsjojo.html', {'news':news})

class NewsUpdate(UpdateView):
	model = Art

	form_class = ArtForm

class NewsDelete(DeleteView):
	model = Art
	success_url ='/news/'
class NewsDetail(DetailView):
	model = Art
	context_object_name = 'art'

def create(request):
	error = ''
	if request.method =="POST":
		form = ArtForm(request.POST)
		if form.is_valid():
			form.save()
			return  redirect('home')
		else:
			error = 'Форма была неверной'
	form = ArtForm()
	data = {
		'form':form,
		'error': error
	}
	return render(request, 'news/art_form.html', data)