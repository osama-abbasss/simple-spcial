from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Group, GroupMember



class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ['name', 'description']
    model = Group
    success_url = reverse_lazy('groups:all_groups')


class DetailGroupView(generic.DetailView):
    model = Group


class GroupListView(generic.ListView):
    model = Group
    template_name = 'groups/group_list.html'



class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single_group', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug= self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user= self.request.user, group= group)
        except:
            print('user already in this grouo')
        else:
            print('joined success')
        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single_group', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(
            user = self.request.user,
            group__slug = self.kwargs.get('slug')
            ).get()
        except GroupMember.DoesNotExist:
            print('member not in this group')

        else:
            membership.delete()
            print('leaved success')

        return super().get(request, *args, **kwargs)
