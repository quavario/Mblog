from collections import ChainMap

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from blog.models import Post, Config


def index(request):
    all_post = Post.objects.order_by('-create_date')

    paginator = Paginator(all_post, 8)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    db_config = Config.objects.all().values('name', 'value')
    context = {}
    for c in db_config:
        context[c['name']] = c['value']
    context['posts'] = page
    print(context)
    return render(request, 'index.html', context)


def index_redirect(request):
    return redirect('/blog/index')


# post
def post_detail(request, id):
    print(id)
    db_post = Post.objects.get(pk=id)
    return render(request, 'post.html', {'post': db_post})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def post(request):
    return render(request, 'index.html')


def config(request):
    if request.user:
        db_config = Config.objects.all().values('name', 'value')
        context = {}
        for c in db_config:
            context[c['name']] = c['value']
        print(context)
        return render(request, 'admin/config.html', context)
    else:
        return redirect('/')


def config_update(request):
    if request.user is None:
        return redirect('/')
    if request.POST:
        blog_title = request.POST['blog_title']
        blog_subtitle = request.POST['blog_subtitle']
        bottom_text = request.POST['bottom_text']

        # set value config
        db_blog_title = Config.objects.get(name='blog_title')
        db_blog_subtitle = Config.objects.get(name='blog_subtitle')
        db_bottom_text = Config.objects.get(name='bottom_text')

        db_blog_title.value = blog_title
        db_blog_subtitle.value = blog_subtitle
        db_bottom_text.value = bottom_text

        # save
        db_blog_subtitle.save()
        db_blog_title.save()
        db_bottom_text.save()
        return HttpResponse('success')


def link_config(request):
    context = {}
    return render(request, 'admin/link_config.html', context)


def link_config_update(request):
    if request.POST:
        wei_url = request.POST['weibo_url']
        github_url = request.POST['github_url']
        facebook_url = request.POST['facebook_url']
