
from django.shortcuts import render

# Create your views here.
def lol(request):
	data = {
		'title' : 'Главная страница',
		'values': ["hello",'my','nigga'],
		'obj':{
			'name':'andrey',
			'surname' : "immersion",
			'hobby': 'dota2'
		}
	}
	return render(request, 'main/index.html',data)

def fak(request):
	return render(request, 'main/fak.html')