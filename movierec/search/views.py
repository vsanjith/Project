from django.shortcuts import render
import requests
from . import config
# Create your views here.
def index(request):

	return render(request,'search.html')
	
def result(request):
	movie_name=request.POST['movie']
	url = 'https://api.themoviedb.org/3/search/movie?api_key='+config.API_KEY+'&query='+movie_name
	r=requests.get(url)
	
	values=r.json()

	return render(request,'results.html',{'values':values})