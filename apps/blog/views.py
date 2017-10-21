from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # __lte: less than equal
    # 投稿日時が現在時刻以下の投稿を抽出
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
