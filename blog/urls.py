from django.urls import path

from .views import blog_detail, blog_list

app_name = 'blog'

urlpatterns = [
    path('list/', blog_list, name='list'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', blog_detail, name='detail'),
]
