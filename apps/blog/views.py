from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView

from .forms import PostForm, CommentForm
from .models import Post


class AddPostView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/add_post.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        return self.render_to_response({ 'form': PostForm() })

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post)


class BlogView(TemplateView):
    template_name = 'blog/blog.html'


class PostView(TemplateView):
    template_name = 'blog/post.html'

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(request.path)
        return self.render_to_response({
                                      'post': post,
                                      'form': form,
                                  })
