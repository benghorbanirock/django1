from django.shortcuts import render, get_object_or_404
from .models import Blog, Tag, Category, Comments
from .forms import CommentForm
from django.core.paginator import Paginator

def blog_list(request):
    blogs = Blog.objects.all()

    paginator=Paginator(blogs,3)
    page_num=request.GET.get('page')
    blog_list=paginator.get_page(page_num) 
    context = {
        'blog_list': blog_list
    }

    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    tags = Tag.objects.filter(blogs=blog)
    recents = Blog.objects.exclude(id=id).order_by('-created_at')[:3]
    category = Category.objects.all()
    comments = Comments.objects.filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_message = form.cleaned_data['message']
            
            new_comment = Comments(blog=blog, name=new_name, email=new_email, message=new_message)
            new_comment.save()

    context = {
        'blog': blog,
        'tags': tags,
        'recents': recents,
        'category': category,
        'comments': comments,
        'form': CommentForm()  # Add the form to the context for rendering
    }

    return render(request, 'blog/blog_detail.html', context)

def blog_tag(request, tag):
    blogs = Blog.objects.filter(tags__slug=tag)

    context = {
        'blogs': blogs
    }

    return render(request, 'blog/blog_list.html', context)

def blog_category(request, category):
    blogs = Blog.objects.filter(category__slug=category)

    context = {
        'blogs': blogs
    }

    return render(request, 'blog/blog_list.html', context)


def search(request):
    if request.method=='GET':
        q=request.GET.get('search')
    blog_list=Blog.objects.filter(title__icontains=q)
    return render(request,'blog/blog_list.html',{'blog_list':blog_list})