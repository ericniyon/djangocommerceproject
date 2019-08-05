from django.views import generic
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
# def home(request):
#     context= {}
#     template = 'home.html'
#     return render(request, template, context)


def about(request):
    context= {}
    template = 'about.html'
    return render(request, template, context)

@login_required
def userProfile(request):
	user = request.user
	context= {'user': user}
	template = 'profile.html'
	return render(request,template,context)

#the functions to desplay postes on my page using generic vieews this desplaylist view

class ListPost(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
#desplay details of our post
class PostDetails(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

