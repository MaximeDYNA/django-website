from django.shortcuts import HttpResponse

def blog_posts(request):
   response = HttpResponse("Contenu test")
   return response