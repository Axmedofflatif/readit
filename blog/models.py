from django.db import models
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models.signals import pre_save
from profiles.models import Profile
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blogs/')
    title = models.CharField(max_length=221)
    slug = models.SlugField(null=True, blank=True, unique_for_date='created_date', max_length=221)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    views = models.IntegerField(default=0, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        url = reverse('blog:detail', kwargs={
            "year": self.created_date.year,
            "month": self.created_date.month,
            "day": self.created_date.day,
            "slug": self.slug
        })
        return url


# class BlogTag(models.Model):
#   blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class SubBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=211)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    contact = models.TextField()

    def __str__(self):
        return self.blog.title


def blog_pre_save(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    return instance


pre_save.connect(blog_pre_save, sender=Blog)
