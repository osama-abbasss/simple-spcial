from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = forms.UserCreateForm
    success_url="/accounts/login/"


class ProfileView(generic.View):
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(models.Profile, PROSlug=kwargs['slug'])
        context = {'profile':profile}
        return render(self.request, 'accounts/profile.html', context)


@login_required
def update_profile_info(request):
    profile = models.Profile.objects.get(PROUser= request.user)
    if request.method == 'POST':
        if request.user == profile.PROUser:
            form = forms.ProfileFrorm(request.POST, request.FILES,instance=profile )
            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                return redirect('/')
    else:
        form = forms.ProfileFrorm(instance=profile)

    context = {'form':form}
    return render(request, 'accounts/update_profile.html', context)
