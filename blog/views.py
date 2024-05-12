from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *



def post_list(request):
    posts=Post.published.all()
    return render(request, "post/post_list.html",{"posts": posts})

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request,'post/post_detail.html',{'post': post})


