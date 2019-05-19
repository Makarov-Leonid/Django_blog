from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForms as TagForm
from .forms import PostForm
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    n = ["oleg","Sasha"]
    return render(request, 'blog/index.html', context = {'posts':posts})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags':tags})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = "blog/post_detail.html"

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = "blog/tag_detail.html"

class TagCreate(ObjCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'

class PostCreate(ObjCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'

class TagUpdate(ObjUpdateMixin,View):
    model_form = TagForm
    model = Tag
    template = 'blog/tag_update_form.html'
