from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from blog.models import BlogPost

@login_required
def blog_posts(request):
   blog_post = get_object_or_404(BlogPost, pk=1)

   return HttpResponse(blog_posts.content)

def home(request):
   return HttpResponse("Page d'acceuil")