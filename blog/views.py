from django.shortcuts import render, get_object_or_404
from .models import Tag, Category, Blog, SubBlog
from django.core.paginator import Paginator


def blog_list(request):
    blogs = Blog.objects.all().order_by('-id')
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if q:
        blogs = blogs.filter(title__icontains=q)
    if tag:
        blogs = blogs.filter(category__title__exact=cat)
    if cat:
        blogs = blogs.filter(tags__title__exact=tag)
    paginator = Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        'object_list': page_obj,
    }

    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, **kwargs):
    slug = kwargs.get('slug', None)
    year = kwargs.get('year', None)
    month = kwargs.get('month', None)
    day = kwargs.get('day', None)
    obj = get_object_or_404(Blog, slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    ctx = {
        'object': obj,
        'categories': categories,
        'tags': tags,
    }

    return render(request, 'blog/blog-single.html', ctx)
