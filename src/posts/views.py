from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from braces.views import SelectRelatedMixin
from . import models, forms

from django.contrib.auth import get_user_model

User = get_user_model()


class PostsList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'group')

class UserPostsList(generic.ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self, *args, **kwargs):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact = self.kwargs.get("username"))
        except User.DoesNotExist:
            return Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(str(self.kwargs['username']))
        context['post_user'] = self.post_user
        return context


class PostDetailView(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))


class PostCreateView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Post
    fields = ['text', 'group']
    success_url = reverse_lazy('posts:all_posts')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all_posts')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)
