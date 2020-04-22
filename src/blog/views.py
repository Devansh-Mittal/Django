from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
# Create your views here.
def home_view(request, *args, **kargs):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'home.html',{'posts':posts}) #string of html code

def product_create_view(request):

	context = {
	}

	return render(request, "product_create.html",context) 