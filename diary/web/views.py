from django.shortcuts import render
from django.http import HttpResponse

from web.models import Article


# Create your views here.
def write(request):
	return render(request, 'write.html')

def new(request):
	x = Article.objects.get_or_create(title=request.GET['title'], content=request.GET['content'])
	return HttpResponse(u'OK')

def home(request):
	ArticleList = Article.objects.all()
	return render(request,"home.html", {'ArticleList': ArticleList})