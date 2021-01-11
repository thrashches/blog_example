from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.contrib import auth

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    title = 'My Blog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


def post_view(request, pk):
    template_name = 'post.html'
    post = get_object_or_404(Post, id=pk)
    form = ''
    if request.user.is_authenticated:
        form = CommentForm()

   # if request.method == 'GET':

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print(form.data)
            comment = Comment()
            comment.post_id = pk
            comment.posted = auth.get_user(request)
            comment.text = form.cleaned_data['text']
            print(comment)
            comment.save()
    return render(request, template_name, {'title': post.title, 'post': post, 'form': form})


def login(request):
    responce = render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = auth.authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            auth.login(request, user)
            print(user)
            responce = redirect('home')
        else:
            responce = redirect('login')

    return responce


def logout(request):
    auth.logout(request)
    return redirect('home')
