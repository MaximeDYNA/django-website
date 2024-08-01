import os
import django
import json

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
django.setup()

from blog.models import BlogPost 

# Load JSON data

chemin = "D:/Dev/workspace/django-projects/website/src/blog_post.json"

with open(chemin, "r", encoding="utf-8") as f:
    data = json.load(f)
    
for bp in data:
    BlogPost.objects.create(title=bp["title"],
                            slug=bp["slug"],
                            published=bp["published"],
                            description=bp["description"],
                            date=bp["date"])

print("Blog posts created successfully.")