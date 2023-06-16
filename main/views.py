from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Blog
from .models import Feedback


def home(request):
    blogs = Blog.objects.order_by('-id')
    page_num = request.GET.get('page', 1)
    paginator = Paginator(blogs, 2)

    page_obj = paginator.page(page_num)

    ctx = {
        'object_list': page_obj,
        'latest_blog': blogs[:2]
    }
    return render(request, 'main/index.html', ctx)


def about(request):
    feedback = Feedback.objects.all()

    ctx = {
        'object_list': feedback
    }

    return render(request, 'main/about.html', ctx)
