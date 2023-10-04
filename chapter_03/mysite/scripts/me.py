from pprint import pprint

from django.db import connection
from django.db.models import Count
from django.contrib.auth.models import User
from django.db.models.functions import Upper, Length

from blog.models import Post

def run():
    posts = Post.objects.annotate(len_name=Length("title"))
    print(vars(posts.first()))
    print(connection.queries)

