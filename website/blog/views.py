from django.contrib.messages.api import success
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model

def home(request):
    return render(request, 'blog/home.html')


class HomeListView(ListView):
    model = Post                        #post_list.html         --default
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post                        #post_list.html         --default
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        UserModel = get_user_model()
        user = get_object_or_404(UserModel, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    success_url = '/'
